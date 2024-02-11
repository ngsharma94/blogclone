from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import User
from .serializers import SignupSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class SignUpView(GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        data = request.data
        serializer = SignupSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Loginview(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            return Response(user.auth_token.key)  # type: ignore
        else:
            return Response(data={'message': 'Invalid email or password'})

    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth)
        }
        return Response(data=content)
    
