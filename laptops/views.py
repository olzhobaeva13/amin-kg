from rest_framework.viewsets import ModelViewSet

from laptops.models import Laptop
from laptops.serializers import LaptopModelSerializer


class LaptopModelViewSet(ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopModelSerializer

