# `django-settings-export`


[![Downloads](https://static.pepy.tech/badge/django-settings-export)](https://pepy.tech/project/django-settings-export)
[![Downloads month](https://static.pepy.tech/badge/django-settings-export/month)](https://pepy.tech/project/django-settings-export)
[![Build status](https://github.com/jkbrzt/django-settings-export/workflows/Build/badge.svg)](https://github.com/jkbrzt/django-settings-export/actions)
[![Coverage](https://coveralls.io/repos/jkbrzt/django-settings-export/badge.svg?branch=master)](https://coveralls.io/r/jkbrzt/django-settings-export?branch=master)
[![PyPi](https://badge.fury.io/py/django-settings-export.svg)](https://pypi.python.org/pypi/django-settings-export)


Often it is needed to make some of your Django project's settings
accessible from within templates. This app provides a simple mechanism
for doing just that.


## Principles

### Explicit is better than implicit

Only explicitly listed settings keys are exported to templates.

### Errors should never pass silently

Accessing an undefined or un-exported setting key from a template results in an exception.




## Installation

Add `'django_settings_export.settings_export'` to  template context processor list in your `settings.py`:

```python
TEMPLATES = [
    {
        # …
        'OPTIONS': {
            'context_processors': [
                # …
                'django_settings_export.settings_export',
            ],
        },
    },
]
```

[Tested on Python 3.8+, Django 2.2+](.github/workflows/test.yml)

## Usage

All settings that should be made accessible from templates need to be
explicitly listed in `settings.SETTINGS_EXPORT`:


```python
# settings.py

DEBUG = True
GA_ID = 'UA-00000-0'

SETTINGS_EXPORT = [
    'DEBUG',
    'GA_ID',
]
```



Now you can access those exported settings from your templates
via `settings.<KEY>`:


```html
<!-- template.html -->

{% if not settings.DEBUG %}
    <script>ga('create', '{{ settings.GA_ID }}', 'auto');</script>
{% endif %}
```

The `settings` variable is an instance of `dict` subclass, so
you use all the methods `dict` provides. For example, you can iterate over
the keys and values using `settings.keys`, `settings.values`,
`settings.items`, etc:

```html
{% for key, value in settings.items %}
    {{ key }}: {{ value }}
{% endfor %}
```


### Changing the `settings` variable name

If you wish to change the name of the context variable to something besides
`settings`, add `SETTINGS_EXPORT_VARIABLE_NAME = 'custom_name'`
to your `settings.py`. This is useful when some other plugin is already adding
`settings` to your template contexts.


```python
# settings.py
FOO = 'bar'
SETTINGS_EXPORT = ['FOO']
SETTINGS_EXPORT_VARIABLE_NAME = 'my_config'
```


```html
<!-- template.html -->

{{ my_config.FOO }}
```

### Exceptions

These custom exceptions can be thrown:

* Listing an undefined setting key in `SETTINGS_EXPORT` results in an `UndefinedSettingError`.
* Accessing an un-exported setting key on the `settings` object in a template results in an `UnexportedSettingError`.

All subclass from `django_settings_export.SettingsExportError`.

## Demo & Tests

See the source code of the bundled [demo app](https://github.com/jkbrzt/django-settings-export/tree/master/tests).


## Development


```bash
$ cd tests

# Run demo
$ python manage.py runserver

# Run tests on current Python
$ python manage.py test
```


## Change Log

See (`CHANGELOG`)[https://github.com/jkbrzt/django-settings-export/blob/master/CHANGELOG.rst].


## Licence

BSD. See [`LICENCE`](https://github.com/jkbrzt/django-settings-export/tree/master/LICENCE) for more details.


## Contact


Jakub Roztocil

* http://roztocil.co
* https://github.com/jkbrzt
* https://twitter.com/jkbrzt


