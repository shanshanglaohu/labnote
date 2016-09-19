from django.db import models
from django.utils.translation import ugettext_lazy as _

from .abstracts import BaseAbstractModel
from .projects import Folder, Project


class NoteBook(BaseAbstractModel):
    """
    the main model of notebooks
    """
    title = models.CharField(_("The title of notebook."), max_length=100)
    body = models.TextField(_("The body of notebook."), blank=True)

    is_published = models.BooleanField(default=False)

    project = models.ForeignKey(Project, blank=True, null=True)
    folder = models.ForeignKey(Folder, blank=True, null=True)


class Text(models.Model):
    text_content = models.TextField(
        _("The text unit of notebook"),
        blank=True
    )

    notebook = models.ForeignKey(NoteBook)


class Table(models.Model):
    """
    table insert into notebook.
    """
    table_name = models.CharField(max_length=50, blank=True)
    table_row = models.PositiveIntegerField(blank=True, null=True)
    table_col = models.PositiveIntegerField(blank=True, null=True)
    table_content = models.TextField(
        _("The table unit of notebook"),
        blank=True
    )

    notebook = models.ForeignKey(NoteBook)


class Attachment(models.Model):
    """
    file or image insert into notebook.
    """
    attachment = models.FileField(upload_to='')