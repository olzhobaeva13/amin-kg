from contacts.views import ContactModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', ContactModelViewSet)


urlpatterns = []

urlpatterns += router.urls
