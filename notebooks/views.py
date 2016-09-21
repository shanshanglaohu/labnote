from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,Group
from django.http import Http404

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from .models import Project, Folder, Table, Text, Notebook, Attachment
from .serializers import ProjectSerializer, FolderSerializer, TableSerializer,\
    TextSerializer, AttachmentSerializer, UserSerializer, GroupSerializer, NotebookSerializer
from .permissions import IsOwnerOrReadOnly


class NotebookList(generics.ListCreateAPIView):
    """
    list all notebooks, or create a new notebook.
    """
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NotebookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a Notebook instance.
    """
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UsersList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    """
    Retrieve one User, or update User profile, or delete User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def _set_lookup_field(self):
        return 'pk' if 'pk' in self.kwargs else 'username'

    lookup_field = property(_set_lookup_field)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserNotebookList(generics.ListAPIView):
    model = Notebook
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer

    def get_queryset(self):
        queryset = super(UserNotebookList, self).get_queryset()
        return queryset.filter(author__pk=self.kwargs.get('pk'))


class GroupList(generics.ListCreateAPIView):
    """
    List groups or create new group, using generic class base view
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    retrieve, update, delete group instance.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def _set_lookup_field(self):
        return 'pk' if 'pk' in self.kwargs else 'name'

    lookup_field = property(_set_lookup_field)
