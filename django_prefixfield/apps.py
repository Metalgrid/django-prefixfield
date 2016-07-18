from __future__ import unicode_literals

from django.apps import AppConfig
from django_prefixfield.fields import PrefixField
from django_prefixfield.lookups import PrefixLookup


class DjangoPrefixfieldConfig(AppConfig):
    name = 'django_prefixfield'
    verbose_name = "Database Prefix Field for Django"

    PrefixField.register_lookup(PrefixLookup)
