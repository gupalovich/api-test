from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models.query import QuerySet
from django_filters.rest_framework import FilterSet
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .utils import serialize_choice_field


class BaseFilter(FilterSet):
    """Base filter to handle ValueError"""

    def filter_queryset(self, queryset):
        try:
            return super().filter_queryset(queryset)
        except ValueError:
            return self.queryset.none()


class CreateInfoMixin:
    @action(detail=False, methods=["get"])
    def add(self, request):
        serializer = self.get_serializer()
        serializer_data = serializer.data

        info_data = {}
        for field_name, field in serializer.fields.items():
            if isinstance(field, serializers.ChoiceField):
                choices = field.choices
                info_data[f"{field_name}_choices"] = serialize_choice_field(choices)
        if info_data:
            serializer_data["info"] = info_data

        return Response(serializer_data)


class UpdateInfoMixin:
    def to_representation(self, instance):
        data = super().to_representation(instance)
        view = self.context.get("view")
        is_detail = view and view.action == "retrieve"

        if is_detail:
            info_data = {}
            for field_name, field in self.fields.items():
                if isinstance(field, serializers.ChoiceField):
                    choices = field.choices
                    info_data[f"{field_name}_choices"] = serialize_choice_field(choices)
                data["info"] = info_data

        return data


class DeleteMultipleSerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField())


class DeleteMultipleMixin:
    @action(detail=False, methods=["delete"])
    def ids(self, request):
        serializer = DeleteMultipleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ids = serializer.validated_data["ids"]
        queryset = self.get_queryset().filter(id__in=ids)

        # Perform permission checks
        for obj in queryset:
            if not self.request.user.has_perm("delete", obj):
                return Response(status=status.HTTP_403_FORBIDDEN)

        # Delete the objects
        queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class VectorSearchMixin:
    def search(self, queryset: QuerySet, search_fields: list) -> QuerySet:
        search_query = self.request.query_params.get("search")
        if search_query:
            search_vector = SearchVector(*search_fields)
            search_query = SearchQuery(search_query)
            queryset = (
                queryset.annotate(search=search_vector, rank=SearchRank(search_vector, search_query))
                .filter(search=search_query)
                .order_by("-rank")
            )
        return queryset
