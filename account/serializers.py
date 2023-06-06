from rest_framework import serializers
from .models import Account, Post, Comment

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'        

class Post_Serializer(serializers.BaseSerializer):
  def to_representation(self,instance):
    return {
      "id":instance.id,
      "content": instance.content,
      "user": instance.user.name,
    }
    
class Comment_Serializer(serializers.BaseSerializer):
    def to_representation(self,instance):
      return {
      "id":instance.id,
      "content": instance.content,
      "user": instance.user.name,
    }