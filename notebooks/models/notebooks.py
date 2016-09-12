from django.db import models
from django.utils.translation import ugettext_lazy as _

from .abstracts import BaseAbstractModel


class NoteBook(BaseAbstractModel):
    """
    the main model of notebooks
    """
    title = models.CharField(_("The title of notebook."), max_length=100)
    body = models.TextField(_("The body of notebook."), blank=True)

    is_published = models.BooleanField(default=False)
