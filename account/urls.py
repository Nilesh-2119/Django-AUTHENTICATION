from django.urls import path
from .views.views import CustomUserView
from .views.login_view import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('register/', CustomUserView.as_view(), name='CustomUserView'),
    path('login/', LoginView.as_view(), name='login'),
    path('tokengenrate/', TokenObtainPairView.as_view(), name='Genrate_Token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token')
]