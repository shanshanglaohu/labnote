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

from .models import Project, Folder, Table, Text, Notebook, Attachment
from .serializers import ProjectSerializer, FolderSerializer, TableSerializer,\
    TextSerializer, AttachmentSerializer, UserSerializer, GroupSerializer, NotebookSerializer


class JSONResponse(HttpResponse):
    """
    an httpresopnse that render its content intp json.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def users_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JSONResponse(serializer.data)


class NotebookList(APIView):
    """
    list all notebooks, or create a new notebook.
    """
    def get(self, request, format=None):
        notebooks = Notebook.objects.all()
        serializer = NotebookSerializer(notebooks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NotebookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotebookDetail(APIView):
    """
    Retrieve, update, or delete a Notebook instance.
    """
    def get_object(self, pk):
        try:
            return Notebook.objects.get(pk=pk)
        except Notebook.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        notebook = self.get_object(pk)
        serializer = NotebookSerializer(notebook)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        notebook = self.get_object(pk)
        serializer = NotebookSerializer(notebook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        notebook = self.get_object(pk)
        notebook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
