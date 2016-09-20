from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import Project, Folder, Notebook, Text, Table, Attachment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder


class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notebook


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
