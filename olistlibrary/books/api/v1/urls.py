from rest_framework.routers import DefaultRouter
from books.api.v1 import views


router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet),
router.register(r'books', views.BookViewSet),

urlpatterns = router.urls
