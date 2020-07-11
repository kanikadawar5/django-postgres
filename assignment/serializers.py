from rest_framework import serializers

from .models import Values


class ValuesSerializer(serializers.HyperlinkedModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     if 'data' in kwargs:
    #         print("data", kwargs['data'], kwargs['data']['key'])
    #         if 'supported_values' in kwargs.get('data'):
    #             kwargs.get('data')['supported_values'] = str(kwargs.get('data')['supported_values'])
    #         if 'type' in kwargs.get('data'):
    #             kwargs.get('data')['type'] = str(kwargs.get('data')['type'])
    #         if 'values' in kwargs.get('data'):
    #             kwargs.get('data')['values'] = str(kwargs.get('data')['values'])
    #     super(ValuesSerializer, self).__init__(*args, **kwargs)

    class Meta:
        model = Values
        fields = ('value_id', 'invalid_trigger', 'key', 'name', 'reuse', 'support_multiple', 'pick_first',
                  'supported_values', 'type', 'validation_parser', 'values', 'create_time')
        read_only_field = None
