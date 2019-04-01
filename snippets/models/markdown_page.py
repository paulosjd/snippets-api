from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from snippets.models.sub_topic import SubTopic


class MarkdownPage(models.Model):

    name = models.CharField(
        max_length=40,
        help_text='',
    )
    sub_topic = models.OneToOneField(
        SubTopic,
        on_delete=models.CASCADE,
    )

    # objects = ActivityManager()

    def __str__(self):
        return '(MarkdownPage) {}'.format(self.name)

    def get_absolute_url(self):
        return reverse(
            'bioactive-actions',
            kwargs={'action': slugify(self.name)}
        )

