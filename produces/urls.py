

from rest_framework.routers import DefaultRouter
from .views import ProduceViewSet

router = DefaultRouter()
router.register(r"produce", ProduceViewSet )
urlpatterns = router.urls
