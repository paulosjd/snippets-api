# coding=utf-8
from rest_framework.generics import ListAPIView
from rest_framework_swagger.views import get_swagger_view

from snippets.models import Category
from snippets.serializers import CategorySerializer


class CategoriesListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.order_by('name').all()
