from rest_framework.routers import DefaultRouter
from .api_views import puzzleViewSet

from .api_views import puzzleLevelViewSet
# from .api_views import LevelTableViewSet

router = DefaultRouter()
router.register(r'puzzles-info', puzzleViewSet,basename='items')
router.register(r'puzzles-level-info',puzzleLevelViewSet,basename='level-items')    
# router.register(r'levels-items',LevelTableViewSet,basename='levels-items')     
urlpatterns = router.urls