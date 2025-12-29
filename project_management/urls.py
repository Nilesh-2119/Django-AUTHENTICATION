from django.urls import path, include
from .views import *
from rest_framework import routers

r = routers.DefaultRouter()
r.register(r'', ProjectView)

urlpatterns =[
    path('', include(r.urls) )
]