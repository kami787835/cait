from rest_framework import generics
from .models import Slider, Direction, Gallery, Laboratory, Base
from .serializers import SliderSerializer, DirectionSerializer, GallerySerializer, LaboratorySerializer, BaseSerializer


class SliderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class DirectionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class LaboratoryListCreateView(generics.ListCreateAPIView):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer


class BaseListCreateView(generics.ListCreateAPIView):
    queryset = Base.objects.all()
    serializer_class = BaseSerializer


class GalleryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
