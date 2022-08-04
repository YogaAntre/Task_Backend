from rest_framework import serializers
from .models import (Texts, Image)

class FileBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Texts
        fields = "__all__"

class CarSingleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']
        
class FileDetailsSerializer(serializers.ModelSerializer):
    image_set=CarSingleImageSerializer(many=True)
    class Meta:
        model = Texts
        fields = ['id','instruction','image_set',"ref_no"]

class FileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"
        

        
