from rest_framework import serializers


class OdorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OdorType
        fields = ('term', )

