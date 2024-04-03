from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework_nested import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)

comments_router = routers.NestedDefaultRouter(router, r'posts')
comments_router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
]
