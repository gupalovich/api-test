from rest_framework.response import Response
from rest_framework.views import APIView


class CarsFilterApiView(APIView):
    def get(self, request):
        return Response(
            {
                "cars": {"data": [], "type": "cars"},
                "filters": [],
                "head_filters": [],
                "info": {},
                "sorting": [],
            }
        )
