# coding=utf-8
from django.db import models

from snippets.models.category import Category


class Topic(models.Model):

    name = models.CharField(
        max_length=20,
        unique=True,
    )
    slug = models.CharField(
        max_length=40,
        db_index=True,
        unique=True,
    )
    completed = models.BooleanField(
        default=False,
        help_text='All content from existing md file'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='topics',
    )
    # objects = SubTopicManager()

    def __str__(self):
        return self.name
