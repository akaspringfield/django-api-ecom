from .models import Items
from rest_framework import serializers
#from django.contrib.auth.hashers import make_password, check_password
#from secrets import token_hex
#import datetime

class ItemsListSerializer(serializers.ModelSerializer):
    
    image = serializers.ImageField(allow_null=True)
    class Meta:
        model = Items
        fields = '__all__'
