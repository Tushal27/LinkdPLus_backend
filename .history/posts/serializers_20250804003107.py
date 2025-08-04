from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='user.first_name')
    author_avatar = serializers.SerializerMethodField()

    def get_author_avatar(self, obj):
        return obj.user.avatar.url

    class Meta:
        model = Posts
        fields = ['id', 'title', 'content', 'author','author_avatar','created', 'likes_count', 'dislikes_count']



    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_dislikes_count(self, obj):
        return obj.dislikes.count()