from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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



class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        """return hello msg"""
        a_viewset=[
         "uses actions(list,create,retriev, updtae,destroy)"
         "returns automatically maps urls using routers"
         "provides more functionality with less code"
        ]

        return Response({'message':"hello",'a_vieset':a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_404_BAD_REQUEST
            )
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})
