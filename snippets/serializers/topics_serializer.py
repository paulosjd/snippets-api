# coding=utf-8
from rest_framework import serializers
from snippets.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('name', 'slug')