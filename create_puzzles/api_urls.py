from rest_framework.routers import DefaultRouter
from .api_views import puzzleViewSet

from .api_views import LimitedItemViewSet
# from .api_views import LevelTableViewSet

router = DefaultRouter()
router.register(r'items', puzzleViewSet,basename='items')
router.register(r'level-items',LimitedItemViewSet,basename='level-items')    
# router.register(r'levels-items',LevelTableViewSet,basename='levels-items')     
urlpatterns = router.urls