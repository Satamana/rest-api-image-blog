from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inst.views import PostView, LikeView, FollowView

router = DefaultRouter()
router.register(r'posts', PostView)
router.register(r'likes', LikeView)
router.register(r'follows', FollowView)

urlpatterns = [
    path('', include(router.urls))
]
