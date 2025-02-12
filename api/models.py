from django.db import models
from django.contrib.auth.models import User  # Required for the ForeignKey reference

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name  # Meaningful string representation

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/%Y/%m/%d/')  # Organize images by date
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery_images", null=True, blank=True)

    def __str__(self):
        return f"Gallery Image ({self.id})"

class Member(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='member_images/%Y/%m/%d/')  # Organize images by date
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Track who added the member
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp

    def __str__(self):
        return f"{self.name} - {self.designation}"
