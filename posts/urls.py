from django.urls import path , include
from rest_framework import routers
from .views import PostsViewSet 

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet , basename='posts'  )

urlpatterns =router.urls