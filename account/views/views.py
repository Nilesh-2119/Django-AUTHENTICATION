from rest_framework.generics import CreateAPIView
from ..models import *
from ..serializers.serializers import *

class CustomUserView(CreateAPIView):
    queryset = CustomUserModel
    serializer_class = CustomUserSerializers