from rest_framework.views import APIView
from rest_framework import response
from ..serializers.login_serializers import LoginSerializers

class LoginView(APIView):
    def post(self, req):
        serializer = LoginSerializers(data = req.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        return response(
            {
                'message' : 'login succefull',
                'username' : user.username,
            }
        )