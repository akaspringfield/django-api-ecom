from .models import Cart
from rest_framework import serializers
#from django.contrib.auth.hashers import make_password, check_password
#from secrets import token_hex
#import datetime

class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
