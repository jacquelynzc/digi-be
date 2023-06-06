from account.views import AllPost_ViewSet,OnePost_ViewSet,Comment_ViewSet
from django.urls import path


urlpatterns = [
    path('posts/', AllPost_ViewSet.as_view()),
    path('posts/<int:id>', OnePost_ViewSet.as_view()),
    path('posts/<int:id>/comments', Comment_ViewSet.as_view()),
]
