from urllib import response
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignUpSerializer
from rest_framework import status
# Register API

class SignUp(APIView):
    def post(self,request):
        reg = SignUpSerializer(data=request.data)
        if reg.is_valid():
             reg.save()
             return Response(reg.data,status=status.HTTP_201_CREATED)
        return Response(400)
      
    
