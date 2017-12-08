from django.db import models


class Timestamp(models.Model):
    """
    The following two fields are common to a lot of models
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
