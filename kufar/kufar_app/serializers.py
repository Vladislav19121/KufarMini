from rest_framework import serializers
from .models import *

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

class PhoneImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneImage
        fields = '__all__'