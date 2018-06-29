from rest_framework.views import APIView
from rest_framework.response import Response


class MyEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'new': 'data'}, status=200)
