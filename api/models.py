from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.description if self.description else 'No description'

class Member(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to='member_images/')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Track who added the member
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.designation}"
