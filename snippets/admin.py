# coding=utf-8
from django.contrib import admin

from snippets.forms import MdSegmentAdminForm
from snippets.models import Category, MarkdownSegment, Topic


class MarkdownTopicFilter(admin.SimpleListFilter):
    title = 'Topic'
    parameter_name = 'id'

    def lookups(self, request, model_admin):
        categories = [(a.id, '{} - {}'.format(a.category, a.name))
                      for a in Topic.objects.order_by('name').distinct()]
        categories.insert(0, ('unassigned', 'Unassigned'))
        return categories

    def queryset(self, request, queryset):
        if self.value() == 'unassigned':
            return queryset.filter(topic__isnull=True)
        if self.value():
            return queryset.filter(topic__id=self.value())
        return queryset.all()


@admin.register(MarkdownSegment)
class MarkdownSegmentAdmin(admin.ModelAdmin):
    list_display = ('get_object_display', 'order')
    list_filter = [MarkdownTopicFilter]
    form = MdSegmentAdminForm
    ordering = ('topic__category__name', 'topic__name', 'name')

    def get_queryset(self, request):
        qs = super(MarkdownSegmentAdmin, self).get_queryset(request)
        return qs.order_by('order')

    def get_object_display(self, obj):
        return '{} - {} - {}'.format(obj.topic.category.name, obj.topic.name, obj.name)


class TopicCategoryFilter(admin.SimpleListFilter):
    title = 'Category'
    parameter_name = 'id'

    def lookups(self, request, model_admin):
        return [(a.id, a.name) for a in Category.objects.order_by('name').distinct()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset.all()


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('get_object_display', 'slug', 'completed')
    list_filter = [TopicCategoryFilter]

    def get_object_display(self, obj):
        return '{} - {}'.format(obj.category.name, obj.name)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
