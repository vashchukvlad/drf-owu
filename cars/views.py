from rest_framework.views import APIView
from rest_framework.response import Response

class CarsView(APIView):
    def get(self, *args, **kwargs):
        return Response({'message': 'Get cars'})
    
    def post(self, *args, **kwargs):
        return Response({'message': 'Post cars'})
    
    def put(self, *args, **kwargs):
        return Response({'message': 'Put cars'})
    
    def patch(self, *args, **kwargs):
        return Response({'message': 'Patch cars'})
    
    def delete(self, *args, **kwargs):
        return Response({'message': 'Delete cars'})