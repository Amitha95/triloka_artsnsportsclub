from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.conf import settings
import os
from urllib.parse import urljoin
from .models import Project, GalleryImage, Member
from .serializers import ProjectSerializer, GalleryImageSerializer, MemberSerializer

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Gallery Image API View
class GalleryImageListView(APIView):
    permission_classes = [AllowAny]  

    def get(self, request):
        media_url = settings.MEDIA_URL
        gallery_images_dir = os.path.join(settings.MEDIA_ROOT, 'gallery_images')

        if os.path.isdir(gallery_images_dir):
            image_files = [f for f in os.listdir(gallery_images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            image_urls = [urljoin(media_url, f'gallery_images/{image}') for image in image_files]
        else:
            image_urls = []

        return Response({'images': image_urls})

# Member Image API View
class MemberImageListView(APIView):
    permission_classes = [AllowAny]  

    def get(self, request):
        media_url = settings.MEDIA_URL
        member_images_dir = os.path.join(settings.MEDIA_ROOT, 'member_images')

        if os.path.isdir(member_images_dir):
            image_files = [f for f in os.listdir(member_images_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            image_urls = [urljoin(media_url, f'member_images/{image}') for image in image_files]
        else:
            image_urls = []

        return Response({'images': image_urls})
