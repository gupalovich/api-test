from rest_framework.response import Response
from rest_framework.views import APIView

from filters.filter import CarFilter


class CarsFilterApiView(APIView):
    def get(self, request):
        response = CarFilter(request=request).get_response()
        return Response(response)
