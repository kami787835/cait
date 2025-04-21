"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .yasg import urlpatterns as yasg_urls
from claider.views import SliderListCreateAPIView,DirectionListCreateAPIView,GalleryListCreateAPIView,LaboratoryListCreateView,BaseListCreateView
from news.views import NewsListCreateAPIView
from contact.views import ContactAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sliders/', SliderListCreateAPIView.as_view(), name='slider-list-create'),
    path('directions/', DirectionListCreateAPIView.as_view(), name='direction-list-create'),
    path('galleries/', GalleryListCreateAPIView.as_view(), name='gallery-list-create'),
    path('laboratories/', LaboratoryListCreateView.as_view(), name='laboratory-list'),
    path('bases/',BaseListCreateView.as_view(), name='scientific-base-list'),
    path('news/', NewsListCreateAPIView.as_view(), name='news-list-create'),
    path('contact/', ContactAPIView.as_view(), name='contact-detail'),

]
urlpatterns += yasg_urls
