# django import
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class BaseAbstractModel(models.Model):

    description = models.TextField("Description")

    first_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseTagAbstractModel(models.Model):
    content_type = models.ForeignKey(ContentType,
                                     related_name="content_type_set_for_%(class)s",
                                     on_delete=models.CASCADE
                                     )
    object_pk = models.TextField("Object ID")
    content_object = GenericForeignKey(ct_field=content_type, fk_field=object_pk)

    class Meta:
        abstract = True
