from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Topic(models.Model):

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
        return '(Topic) {}'.format(self.name)

    def get_absolute_url(self):
        return reverse(
            'bioactive-actions',
            kwargs={'action': slugify(self.name)}
        )

