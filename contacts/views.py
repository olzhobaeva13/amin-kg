from rest_framework.viewsets import ModelViewSet

from contacts.models import Contact
from contacts.serializers import ContactModelSerializer


class ContactModelViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
