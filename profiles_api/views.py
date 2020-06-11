from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    """Test APIView"""
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        """returns a list of apiview features"""
        an_apiview=[
        'Uses HTTP methods as function(get,post,patch,put,delete)'
        'is similar to django view'
        'gives you the most control over app logic'
        'is mapped manually to url'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """create hello msg with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello{name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """updates partial"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})
