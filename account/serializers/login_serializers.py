from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        u = data.get('username')
        p = data.get('password')

        user = authenticate(username = u, password = p)
        
        if not user:
            raise serializers.ValidationError('Invalid user')
        
        data['user'] = user
        return data