from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ItemsListSerializer
from .models import Items

class ItemsList(generics.ListAPIView):
    #hear we geting the user model as object
    queryset = Items.objects.order_by('created_at').reverse().filter(status='active')
    serializer_class = ItemsListSerializer



