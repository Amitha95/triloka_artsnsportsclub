from rest_framework import serializers
from django.conf import settings
from .models import Project, GalleryImage, Member  # Import Member model

class GalleryImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()  # Custom field for full image URL

    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'image_url', 'description']

    def get_image_url(self, obj):
        request = self.context.get('request')  # Get request object if available
        if request is not None:
            return request.build_absolute_uri(obj.image.url)  # Return full URL with domain
        return settings.MEDIA_URL + str(obj.image)  # Fallback to relative URL

class ProjectSerializer(serializers.ModelSerializer):
    gallery_images = GalleryImageSerializer(many=True, read_only=True)  # Include images in the project response

    class Meta:
        model = Project
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    added_by = serializers.StringRelatedField()  # Show username instead of ID

    class Meta:
        model = Member
        fields = ['id', 'name', 'designation', 'image', 'image_url', 'added_by', 'created_at']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        return settings.MEDIA_URL + str(obj.image)

