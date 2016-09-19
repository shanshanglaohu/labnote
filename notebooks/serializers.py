from rest_framework import serializers

from .models import Project, Folder, NoteBook, Text, Table, Attachment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder


class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteBook


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
