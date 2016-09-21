from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, Group

from .abstracts import BaseAbstractModel
from .projects import Folder, Project


@python_2_unicode_compatible
class Notebook(BaseAbstractModel):
    """
    the main model of Notebooks
    """
    title = models.CharField(_("The title of Notebook."), max_length=100)
    body = models.TextField(_("The body of Notebook."), blank=True)

    is_published = models.BooleanField(default=False)

    project = models.ForeignKey(Project, blank=True, null=True)
    folder = models.ForeignKey(Folder, blank=True, null=True)
    author = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE, related_name='notebooks'
    )
    Group = models.ForeignKey(Group, blank=True, null=True)

    def __str__(self):
        return self.title


class Text(models.Model):
    text_content = models.TextField(
        _("The text unit of Notebook"),
        blank=True
    )

    notebook = models.ForeignKey(Notebook, blank=True, null=True)


class Table(models.Model):
    """
    table insert into Notebook.
    """
    table_name = models.CharField(max_length=50, blank=True)
    table_row = models.PositiveIntegerField(blank=True, null=True)
    table_col = models.PositiveIntegerField(blank=True, null=True)
    table_content = models.TextField(
        _("The table unit of Notebook"),
        blank=True
    )

    notebook = models.ForeignKey(Notebook, blank=True, null=True)


class Attachment(models.Model):
    """
    file or image insert into Notebook.
    """
    attachment = models.FileField(upload_to='')

    notebook = models.ForeignKey(Notebook, blank=True, null=True)

    author = models.ForeignKey(User, blank=True, null=True)

    group = models.ForeignKey(Group, blank=True, null=True)