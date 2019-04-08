# coding=utf-8
from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=40,
        help_text='e.g. Django',
        db_index=True,
    )
    logo = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
