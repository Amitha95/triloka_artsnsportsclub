from rest_framework import viewsets
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Project, GalleryImage, Member
from .serializers import ProjectSerializer, GalleryImageSerializer, MemberSerializer



class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Require authentication


def project_list(request):
    data = {"projects": [{"id": 1, "name": "Project A"}, {"id": 2, "name": "Project B"}]}
    return JsonResponse(data)

@csrf_exempt  # Only use this if necessary, otherwise use proper CSRF handling
def get_gallery_images(request):
    media_root = settings.MEDIA_ROOT
    media_url = settings.MEDIA_URL
    gallery_images_dir = os.path.join(media_root, 'gallery_images')

    # List all valid image files
    if os.path.isdir(gallery_images_dir):
        image_files = [f for f in os.listdir(gallery_images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        # Construct full URLs for the images
        image_urls = [os.path.join(media_url, 'gallery_images', image) for image in image_files]
    else:
        image_urls = []

    return JsonResponse({'images': image_urls})

@csrf_exempt  # Only use if necessary, otherwise use DRF's APIView for better handling
def get_member_images(request):
    media_root = settings.MEDIA_ROOT
    media_url = settings.MEDIA_URL
    member_images_dir = os.path.join(media_root, 'member_images')

    if os.path.isdir(member_images_dir):
        image_files = [f for f in os.listdir(member_images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        image_urls = [os.path.join(media_url, 'member_images', image) for image in image_files]
    else:
        image_urls = []

    return JsonResponse({'images': image_urls})

