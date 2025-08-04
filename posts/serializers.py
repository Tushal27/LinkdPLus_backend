from rest_framework import serializers
from .models import Posts , Comments

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    author_avatar = serializers.SerializerMethodField()
    def get_author_avatar(self, obj):
        return obj.user.avatar.url
    def get_author(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    class Meta:
        model = Comments
        fields = ['id','user', 'content', 'author', 'author_avatar', 'created']
        read_only_fields = ['id','user','created']

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    author_avatar = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    def get_author_avatar(self, obj):
        return obj.user.avatar.url
    def get_author(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'comments','author','author_avatar','created', 'likes_count', 'dislikes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_dislikes_count(self, obj):
        return obj.dislikes.count()
    
