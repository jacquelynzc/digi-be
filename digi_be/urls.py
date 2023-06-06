from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from account.views import AccountViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', include('user_auth.urls')),
    path('admin/', admin.site.urls),
]
