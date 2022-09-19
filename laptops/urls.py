from laptops.views import LaptopModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', LaptopModelViewSet)


urlpatterns = []

urlpatterns += router.urls
