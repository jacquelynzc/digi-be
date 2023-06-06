from .serializers import AccountSerializer, PostSerializer, CommentSerializer
from .models import Account, Post, Comment
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer    

class AllPost_ViewSet(APIView):
  permission_classes = [
    permissions.AllowAny
  ]
  def post(self,request):
    try:
      user = self.request.user
      isAuthenticated = user.is_authenticated
      if isAuthenticated: 
          content = request.data['content']
          caption = request.data.get('image')
          # This is to get the profile of the user who is making this post
          userProfile = Account.objects.get(user=user)
          Post.objects.create(user=userProfile, content=content, caption=caption)
          return Response({'message': " ◕‿↼ Post Successfully Created ! "})
      else:
          return Response({'error': "ヽ(ﾟДﾟ)ﾉ  not authenticated make sure you include a token"})
    except:
          return Response({'error': "( ﾟДﾟ)b error; you are most likely messed up by passing an invaild body"})
  def get(self, request): 
    try:
      results = Post.objects.all()
      all_post = PostSerializer(results, many=True)
      return Response(all_post.data)
    except:
      return Response({"error": "( ﾟДﾟ)b  somthing went wrong "})
  
class OnePost_ViewSet(APIView):
  permission_classes = [
    permissions.AllowAny
  ]
  def get(self, request,id):
    try:
      post_results = Post.objects.get(id=id)
      post = PostSerializer(post_results)
      comments_results = Comment.objects.filter(post=id)
      comments = CommentSerializer(comments_results, many=True)
      return Response({"post":post.data,"comments":comments.data})
    except:
      return Response({"error": "( ﾟДﾟ)b  somthing went wrong "})
  
class Comment_ViewSet(APIView):
  permission_classes = [
    permissions.AllowAny
  ]
  def post(self,request,id):
    try:
      user = self.request.user
      isAuthenticated = user.is_authenticated
      if isAuthenticated:
          content = request.data['content']
          # This is to get the profile of the user who is making this post
          userProfile = Account.objects.get(user=user)
          post = Post.objects.get(id=id)
          Comment.objects.create(user=userProfile, content=content,post=post)
          return Response({'message': " ◕‿↼ Comment Successfully Created ! "})
      else:
          return Response({'error': "ヽ(ﾟДﾟ)ﾉ  not authenticated make sure you include a token"})
    except:
          return Response({'error': "( ﾟДﾟ)b error; you are most likely messed up by passing an invaild body"})