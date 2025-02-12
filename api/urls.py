from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, GalleryImageListView, MemberImageListView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include all registered viewsets
    path('api/gallery-images/', GalleryImageListView.as_view(), name='gallery-image-list'),
    path('api/member-images/', MemberImageListView.as_view(), name='member-image-list'),
]
