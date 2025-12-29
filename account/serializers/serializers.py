from rest_framework import serializers
from ..models import CustomUserModel

class CustomUserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        return CustomUserModel.objects.create_user(
            username=validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password'],
            
        )