from rest_framework import serializers

from .models import Values


class ValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Values
        fields = ('value_id', 'invalid_trigger', 'key', 'name', 'reuse', 'support_multiple', 'pick_first',
                  'supported_values', 'type', 'validation_parser', 'values', 'create_time')
        read_only_field = None
