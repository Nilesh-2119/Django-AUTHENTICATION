from django.urls import path
from .views.views import CustomUserView
from .views.login_view import LoginView
urlpatterns = [
    path('register/', CustomUserView.as_view(), name='CustomUserView'),
    path('login/', LoginView.as_view(), name='login'),
]