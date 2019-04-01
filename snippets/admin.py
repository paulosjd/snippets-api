from django.contrib import admin

from snippets.models import MarkdownPage, MarkdownSegment, SubTopic, Topic


@admin.register(MarkdownPage)
class MarkdownPageAdmin(admin.ModelAdmin):
    pass


@admin.register(MarkdownSegment)
class MarkdownSegmentAdmin(admin.ModelAdmin):
    pass


@admin.register(SubTopic)
class SubTopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

