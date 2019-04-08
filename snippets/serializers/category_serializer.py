# coding=utf-8
from rest_framework import serializers
from snippets.models import Category
from snippets.serializers.topics_serializer import TopicSerializer


class CategorySerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'logo', 'topics')

