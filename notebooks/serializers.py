from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import Project, Folder, Notebook, Text, Table, Attachment


class UserSerializer(serializers.ModelSerializer):
    # notebooks = serializers.HyperlinkedIdentityField(
    #     many=True, view_name='user-notebook-list', read_only=True
    # )

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


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
    author = serializers.ReadOnlyField(source='author.username')

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
