from django.urls import path
from .views import *

urlpatterns = [
    path('slider/', SliderListCreateAPIView.as_view()),
    path('direction',DirectionListCreateAPIView.as_view()),
    path('gallery/', GalleryListCreateAPIView.as_view()),
    path('laboratory', LaboratoryListCreateView.as_view()),
    path('base',BaseListCreateView.as_view())
]