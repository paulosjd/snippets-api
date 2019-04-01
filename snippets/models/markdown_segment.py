from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from snippets.models.markdown_page import MarkdownPage

class MarkdownSegment(models.Model):

    name = models.CharField(
        max_length=100,
        help_text='e.g. snippet - redux async action creator',
    )
    order = models.IntegerField(
        help_text='Int asc. order',
        unique=True,
        db_index=True,
    )
    keywords = ArrayField(
        models.CharField(max_length=50),
        null=True,
        blank=True,
    )
    content = models.TextField(
        max_length=8000,
    )
    markdown_page = models.ForeignKey(
        MarkdownPage,
        related_name='segments',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '(MarkdownSegment) {}'.format(self.name)

    def get_absolute_url(self):
        return reverse(
            'bioactive-actions',
            kwargs={'action': slugify(self.name)}
        )

