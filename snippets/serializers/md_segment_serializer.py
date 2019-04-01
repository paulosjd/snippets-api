from rest_framework import serializers
from snippets.models import MarkdownPage, MarkdownSegment


class MarkdownSegmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarkdownPage
        fields = ('term', )


class CompoundSerializer(serializers.ModelSerializer):
    odor_categories = OdorTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Odorant
        fields = ('cas_number', 'smiles', 'iupac_name', 'chemical_name', 'chemical_properties', 'odor_categories', )
