from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = Post

class VeriyEmailSerializer(serializers.Serializer):
    key = serializers.CharField(write_only=True)