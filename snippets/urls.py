from django.urls import include, path
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetViewSet, UserViewSet

router = DefaultRouter()
router.register(r"snippets", SnippetViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [path("", include(router.urls))]
