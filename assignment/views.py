from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import ValuesSerializer
from .models import Values
from typing import List, Dict, Callable, Tuple

SlotValidationResult = Tuple[bool, bool, str, Dict]


def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                  invalid_trigger: str = None, key: str = None,
                                  support_multiple: bool = True, pick_first: bool = False, type_name: str = "",
                                  **kwargs) -> SlotValidationResult:
    ids_stated = []
    trigger = invalid_trigger
    partially_filled = False
    total_values = len(values)
    values_checked = 0
    filled = False
    parameters = {key: ids_stated}

    for value in values:
        if 'entity_type' in value and 'value' in value:
            partially_filled = True
        if value['value'] not in supported_values:
            trigger = invalid_trigger
            parameters = {}
            break

        elif value['value'] in supported_values:
            partially_filled = True
            values_checked += 1
            ids_stated.append(value['value'])

    if values_checked == total_values and total_values != 0:
        filled = True
        trigger = ""
        partially_filled = False
    if pick_first is True and len(ids_stated) > 0:
        age_stated = ids_stated[0]
        parameters[key] = age_stated
    elif support_multiple is True:
        age_stated = ids_stated
        parameters[key] = age_stated

    result = {
        'filled': filled,
        'partially_filled': partially_filled,
        'trigger': trigger,
        'parameters': parameters
    }
    return result


def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                            support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None,
                            **kwargs) -> SlotValidationResult:
    age_stated = []
    trigger = invalid_trigger
    partially_filled = False
    total_values = len(values)
    values_checked = 0
    filled = False
    parameters = {}

    for value in values:
        if not isinstance(value['value'], int):
            parameters = {}
            break
        if 'entity_type' in value and 'value' in value:
            partially_filled = True
            vars()[var_name] = value['value']
            if eval(constraint):
                trigger = ""
                partially_filled = True
                values_checked += 1
                age_stated.append(value['value'])
            else:
                trigger = invalid_trigger

    if values_checked == total_values and total_values != 0:
        filled = True
        trigger = ""
        partially_filled = False
    if pick_first is True and len(age_stated) > 0:
        age_stated = age_stated[0]
        parameters[key] = age_stated
    elif support_multiple is True:
        age_stated = age_stated
        parameters[key] = age_stated

    if total_values == 0:
        parameters = {}

    result = {
        'filled': filled,
        'partially_filled': partially_filled,
        'trigger': trigger,
        'parameters': parameters
    }
    return result


class ValuesSet(viewsets.ModelViewSet):
    queryset = Values.objects.all().order_by('value_id')
    serializer_class = ValuesSerializer

    def perform_create(self, serializer):
        try:
            return serializer.save()
        except:
            message = "Error while creating"
            raise ValueError(message)

    def create(self, request, *args, **kwargs):
        try:
            result = {
                "status_code": 200,
                "message": "",
                "data": {}
            }
            data = request.data
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():

                self.perform_create(serializer)
                if 'validation_parser' in data:
                    if data['validation_parser'] == 'finite_values_entity':
                        if all(k in data for k in ("values", "supported_values", "invalid_trigger", "key",
                                                   "support_multiple", "pick_first")):
                            result = validate_finite_values_entity(data['values'], data['supported_values'],
                                                                   data['invalid_trigger'], data['key'],
                                                                   data['support_multiple'],
                                                                   data['pick_first'], data['type'])
                            return Response(result)
                    elif data['validation_parser'] == 'numeric_values_entity':
                        support_multiple = data.get('support_multiple') or False
                        pick_first = data.get('pick_first') or False

                        result = validate_numeric_entity(data['values'], data['invalid_trigger'], data['key'],
                                                         support_multiple, pick_first,
                                                         data['constraint'], data['var_name'])
                        return Response(result)
                    else:
                        result['message'] = "I - (values, supported_values, invalid_trigger, key, support_multiple, " \
                                            "pick_first) or II-(values, invalid_trigger, key, " \
                                            "support_multiple, pick_first, constraint, var_name) is required"
                        result['status_code'] = 400
                        return Response(result)
        except ValueError as e:
            result = {
                "status_code": 400,
                "message": str(e),
                "data": {}
            }
            return Response(result)
