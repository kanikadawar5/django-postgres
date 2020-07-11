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
                                  support_multiple: bool = True, pick_first: bool = False,
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
    if pick_first is True:
        ids_stated = str(ids_stated['0'])
    elif support_multiple is True:
        ids_stated = ids_stated

    SlotValidationResult = {
        'filled': filled,
        'partially_filled': partially_filled,
        'trigger': trigger,
        'parameters': parameters
    }
    return SlotValidationResult
    # """
    # Validate an entity on the basis of its value extracted.
    # The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").
    #
    # :param pick_first: Set to true if the first value is to be picked up
    # :param support_multiple: Set to true if multiple utterances of an entity are supported
    # :param values: Values extracted by NLU
    # :param supported_values: List of supported values for the slot
    # :param invalid_trigger: Trigger to use if the extracted value is not supported
    # :param key: Dict key to use in the params returned
    # :return: a tuple of (filled, partially_filled, trigger, params)
    # """
    # ...


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
                # if 'values' in data and 'supported_values' in data and :
                if all(k in data for k in ("values", "supported_values", "invalid_trigger", "key", "support_multiple",
                                           "pick_first")):
                    SlotValidationResult = validate_finite_values_entity(data['values'], data['supported_values'], data['invalid_trigger'],
                                                  data['key'], data['support_multiple'], data['pick_first'])
                    return Response(SlotValidationResult)
                else:
                    result['message'] = "values, supported_values, invalid_trigger, key, support_multiple, " \
                                        "pick_first are required"
                    result['status_code'] = 400
                    return Response(result)
                result['status_code'] = 200
                result['message'] = "User created"
                print("seri", serializer.data['value_id'])
                result["data"] = {"value_id": serializer.data['value_id']}
                return Response(result)
            else:
                error = serializer.errors
                result['message'] = error
                return Response(result)
            result['message'] = "User created"
            result['data'] = data
            return Response(result)
        except ValueError as e:
            result = {
                "status_code": 400,
                "message": str(e),
                "data": {}
            }
            return Response(result)
