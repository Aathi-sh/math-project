from rest_framework.routers import DefaultRouter
from .api_views import ItemViewSet

from .api_views import LimitedItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet,basename='item')
router.register(r'level-items',LimitedItemViewSet,basename='level-items')
urlpatterns = router.urls
      
