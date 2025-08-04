from rest_framework.routers import DefaultRouter
from .views import ContactMessageView
router = DefaultRouter()
router.register(r'contactme', ContactMessageView , basename='contactme'  )

urlpatterns = router.urls