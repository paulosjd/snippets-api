# coding=utf-8
from rest_framework import serializers
from snippets.models import MarkdownSegment


class MarkdownSegmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarkdownSegment
        fields = ('order', 'keywords', 'content')

