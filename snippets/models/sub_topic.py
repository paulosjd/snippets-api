from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from snippets.models.topic import Topic


class SubTopic(models.Model):

    name = models.CharField(
        max_length=40,
        help_text='',
        db_index=True,
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='subtopics',
    )
    keywords = ArrayField(
        models.CharField(max_length=100),
        null=True,
        blank=True,
    )
    # objects = SubTopicManager()

    def __str__(self):
        return '(SubTopic) {}'.format(self.name)

    def get_absolute_url(self):
        return reverse(
            'bioactive-actions',
            kwargs={'action': slugify(self.name)}
        )

