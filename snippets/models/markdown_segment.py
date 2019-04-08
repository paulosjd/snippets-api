# coding=utf-8
from django.contrib.postgres.fields import ArrayField
from django.db import models


class MarkdownSegment(models.Model):

    name = models.CharField(
        max_length=100,
        help_text='e.g. snippet - redux async action creator',
    )
    order = models.IntegerField(
        help_text='Int asc. order',
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
    topic = models.ForeignKey(
        'snippets.Topic',
        related_name='segments',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ('order', 'topic')

    def __str__(self):
        return '(MarkdownSegment) {}'.format(self.name)
