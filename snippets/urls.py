# coding=utf-8
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import CategoriesListView, TopicSegmentsView, schema_view


urlpatterns = [
    path('categories', CategoriesListView.as_view()),
    path('topics/<slug>', TopicSegmentsView.as_view()),
    path('docs/', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
