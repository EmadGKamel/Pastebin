from app.models import Snippet
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ( 'id', 'owner', 'title', 'content', 'creation_date', 'expiration_date', 'exposure_status',)
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'groups',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ( 'name',)