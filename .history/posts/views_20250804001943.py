from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Posts
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by("-id")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        Posts = self.get_object()
        user = request.user
        if user in Posts.likes.all():
            Posts.likes.remove(user) 
            liked = False 
        else:
            Posts.likes.add(user)
            Posts.dislikes.remove(user)
            liked = True
        return Response({"liked": liked, "likes_count": Posts.likes.count(),"dislikes_count": Posts.dislikes.count()})

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        Posts = self.get_object()
        user = request.user
        if user in Posts.dislikes.all():
            Posts.dislikes.remove(user)
            disliked = False
        else:
            Posts.dislikes.add(user)
            Posts.likes.remove(user)
            disliked = True
        return Response({'disliked': disliked, 'likes_count': Posts.likes.count(), 'dislikes_count': Posts.dislikes.count()})