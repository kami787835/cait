from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer