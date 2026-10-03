from rest_framework import serializers
from .models import BaseModel

class BaseSerial(serializers.ModelSerializer):
    class Meta:
        model = BaseModel
        fields = ['id','title','slug','text','author','created']