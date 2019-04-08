from django.forms import ModelForm, ModelChoiceField

from snippets.models.topic import Topic
from snippets.models.markdown_segment import MarkdownSegment


class TopicModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} - {}".format(obj.category.name, obj.name)


class MdSegmentAdminForm(ModelForm):
    topic = TopicModelChoiceField(queryset=Topic.objects.order_by('category__name', 'name'))

    def __init__(self, *args, **kwargs):
        super(MdSegmentAdminForm, self).__init__(*args, **kwargs)
        self.fields['content'].strip = False

    class Meta:
        model = MarkdownSegment
        fields = "__all__"
