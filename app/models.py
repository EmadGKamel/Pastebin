from .helpers import url_shortner
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

class Snippet(models.Model):
    id = models.CharField(primary_key=True, max_length=19, default=url_shortner, editable=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="Untitled")
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    exposure_status = models.BooleanField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:snippet-detail', kwargs={'pk': self.pk})


