from api.serializers import SnippetSerializer, UserSerializer, GroupSerializer
from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from app.models import Snippet, CustomUser


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
