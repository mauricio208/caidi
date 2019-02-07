from rest_framework import routers
from homepage.viewsets import ArticleViewSet

router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)