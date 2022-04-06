from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register(
    r'api/v1/posts/(?P<post_id>.+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
