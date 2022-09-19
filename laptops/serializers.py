from rest_framework import serializers
from laptops.models import Laptop


class LaptopModelSerializer(serializers.ModelField):

    class Meta:
        model = Laptop
        fields = '__all__'
