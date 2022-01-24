from django.shortcuts import render
# Create your views here.

from typing import Generic
from rest_framework import generics
from .serializers import UserSignUpSerializer, UserSignInSerializer
from .models import User

class UserSignUp(generics.CreateAPIView):
    #hear we geting the user model as object
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

class UserSignIn(generics.CreateAPIView):
    #hear we geting the user model as object
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer

