from django.urls import path
from .views import *



urlpatterns = [
    path('contact/', ContactAPIView.as_view())
]
