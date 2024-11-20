from rest_framework import serializers
from .models import User
 
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5)
    class Meta:
        model = User
        fields = ['user_id','user_img','username']