from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test APIView"""
    def get(self,request,format=None):
        """returns a list of apiview features"""
        an_apiview=[
        'Uses HTTP methods as function(get,post,patch,put,delete)'
        'is similar to django view'
        'gives you the most control over app logic'
        'is mapped manually to url'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
