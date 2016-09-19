from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User, Group

from mptt.models import MPTTModel, TreeForeignKey

from .abstracts import BaseAbstractModel


@python_2_unicode_compatible
class Project(BaseAbstractModel):
    """
    Organize Research with projects.
    """
    name = models.CharField(
        _('Project name'),
        max_length=50,
        help_text=_("The name of project, which contain only numbers, alphabets and underscores")
    )

    # todo: write a User pro application and change the foreignkey to new user model
    author = models.ForeignKey(User)
    team = models.ForeignKey(Group, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


@python_2_unicode_compatible
class Folder(MPTTModel, BaseAbstractModel):
    """

    """
    name = models.CharField(
        _("Folder name"),
        max_length=50,
        help_text=_("The name of folder.")
    )

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    project = models.ForeignKey(Project, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Folder")
        verbose_name_plural = _("Folders")
