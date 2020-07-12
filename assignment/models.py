from django.db import models

# from django_mysql.models import JSONField, Model

# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

# from django_mysql.models import ListCharField
# from djangotoolbox.fields import ListField

def my_default():
    return {'foo': 'bar'}


class Values(models.Model):
    value_id = models.AutoField(verbose_name="Value ID", primary_key=True)
    invalid_trigger = models.CharField(verbose_name="invalid_trigger", max_length=100, blank=True, null=True)
    key = models.CharField(verbose_name="key", max_length=100, blank=True, null=True)
    name = models.CharField(verbose_name="name", max_length=150, blank=True)
    reuse = models.BooleanField(verbose_name="reuse", blank=True, null=True)
    support_multiple = models.BooleanField(verbose_name="support_multiple", blank=True, null=True)
    pick_first = models.BooleanField(verbose_name="pick_first", blank=True, null=True)
    supported_values = ArrayField(models.CharField(max_length=20, blank=True, null=True),
                                  verbose_name="supported_values", blank=True, null=True)
    type = ArrayField(models.CharField(max_length=20, blank=True, null=True), verbose_name="type",
                      blank=True, null=True)
    validation_parser = models.CharField(verbose_name="validation_parser", max_length=150, blank=True, null=True)
    values = ArrayField(JSONField(default=my_default), verbose_name="values", blank=True, null=True)
    constraint = models.CharField(verbose_name="Constraint", max_length=200, blank=True, null=True)
    var_name = models.CharField(verbose_name="var_name", max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'values_requests'
        verbose_name = "Kanika Dawar Assignment"
        # ordering = ("value_id", )

# {
#   "invalid_trigger": "invalid_ids_stated",
#   "key": "ids_stated",
#   "name": "govt_id",
#   "reuse": true,
#   "support_multiple": true,
#   "pick_first": false,
#   "supported_values": [
#     "pan",
#     "aadhaar",
#     "college",
#     "corporate",
#     "dl",
#     "voter",
#     "passport",
#     "local"
#   ],
#   "type": [
#     "id"
#   ],
#   "validation_parser": "finite_values_entity",
#   "values": [
#     {
#       "entity_type": "id",
#       "value": "college"
#     }
#   ]
# }

# {
#   "invalid_trigger": "invalid_age",
#   "key": "age_stated",
#   "name": "age",
#   "reuse": true,
#   "pick_first": true,
#   "type": [
#     "number"
#   ],
#   "validation_parser": "numeric_values_entity",
#   "constraint": "x>=18 and x<=30",
#   "var_name": "x",
#   "values": [
#     {
#       "entity_type": "number",
#       "value": 23
#     }
#   ]
# }

# python manage.py sqlmigrate assignment 0001_initial
# values: List[Dict], invalid_trigger: str = None, key: str = None,
# support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None