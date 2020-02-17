from .views import CharacterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CharacterViewSet, basename='characters')
router.register(r'characters', CharacterViewSet, basename='characters')
urlpatterns = router.urls
