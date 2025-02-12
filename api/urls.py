from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, GalleryImageViewSet, MemberViewSet, project_list, get_gallery_images,get_member_images

# Set up the router and register the viewsets
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'gallery-images', GalleryImageViewSet)  
router.register(r'members', MemberViewSet)  # Registering MemberViewSet

urlpatterns = [
    path('', include(router.urls)),  # Includes all registered viewsets (projects, gallery-images, members)
    path('api/projects/', project_list, name='project-list'),
    path('api/gallery-images/', get_gallery_images, name='gallery-image-list'),
    path('api/member-images/', get_member_images, name='member-image-list'),


]
