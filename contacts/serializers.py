from rest_framework.serializers import ModelSerializer
from contacts.models import Contact


class ContactModelSerializer(ModelSerializer):
    
    class Meta:
        model = Contact
        exclude = ('map_picture', )
        # fields = '__all__'
