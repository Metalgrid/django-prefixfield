# Django Prefix Field

--------------------------------------------------------------------------------

## Overview

Adds a Prefix field to use with Django models. Useful for applications that require matching prefixes against the search criteria, e.g. a telephony billing application where you need to find the carrier prefix from the whole telephone number.

The `PrefixField` is indexed by default and supports [PostgreSQL Prefix](https://github.com/dimitri/prefix) if available.

## Installation

1. Install via pip: `pip install django_prefixfield`
2. Add `django_prefixfield` to your `INSTALLED_APPS` in `settings.py`

## Usage

### Creating a prefix field

```
# models.py
from django_prefixfield.fields import PrefixField

class MyModel(models.Model):
    code = PrefixField(max_length=16)
```

### Querying prefixes

Use the `prefix` lookup:

```
# instance is a model of MyModel
instance.objects.filter(code__prefix='12345678901234')
```

### Using the `prefix` lookup with `CharField`/`TextField`

Prefixes are subclassed from `CharField` so they are compatible with all operations available to them. If you have a `CharField` and don't want to change your model, you can register the `prefix` lookup instead.

```
from django.db.models import CharField
from django_prefixfield.lookups import PrefixLookup
# ...
CharField.register_lookup(PrefixLookup)
```

## License

django_prefixfield is distributed under the MIT license. Please see LICENSE.txt

## Author

Iskren Hadzhinedev (Metalgrid)

## Version history

- 0.1.2

  - Removed redundant subquery when looking for [PostgreSQL Prefix](https://github.com/dimitri/prefix)

- 0.1.1

  - Add documentation

- 0.1.0

  - Support all django db backends
  - Support [PostgreSQL Prefix](https://github.com/dimitri/prefix)
  - Autoindex by default
