from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass


@admin.register(Notebook)
class NoteBookAdmin(admin.ModelAdmin):
    pass


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Attachment)
class Attachment(admin.ModelAdmin):
    pass
