``django-settings-export``
##########################


|version| |travis| |coverage|


Often it is needed to make some of your Django project's settings
accessible from within templates. This app provides a simple mechanism
for doing just that.


**Principles:**

* *Explicit is better than implicit:* Only explicitly listed
  settings keys are exported to templates.
* *Errors should never pass silently:* Accessing an undefined
  or unexported setting key from a template results in an exception.


Tested on Python 2.7+, Django 1.5+.


Installation
============

.. code-block:: bash

    $ pip install django-settings-export


Add ``'django_settings_export.settings_export'`` to
template context processor list in your ``settings.py``:

**Django 1.8 and newer:**

.. code-block:: python

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

**Django older than 1.8:**

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = [
        # [...]
        'django_settings_export.settings_export',
    ]



Usage
=====

All settings that should be made accessible from templates need to be
explicitly listed in ``settings.SETTINGS_EXPORT``:


.. code-block:: python

    # settings.py

    DEBUG = True
    GA_ID = 'UA-00000-0'

    SETTINGS_EXPORT = [
        'DEBUG',
        'GA_ID',
    ]



Now you can access those exported settings from your templates
via ``settings.<KEY>``:


.. code-block:: html

    {% if not settings.DEBUG %}
        <script>ga('create', '{{ settings.GA_ID }}', 'auto');</script>
    {% endif %}


**Exceptions:**

* Listing an undefined setting key in ``SETTINGS_EXPORT`` results in an
  ``UndefinedSettingError``.
* Accessing a unexported setting key on the ``settings`` object in a template
  results in an ``UnexportedSettingError``.

If you wish to change the name of the context variable to something besides
``settings``, add ``SETTINGS_EXPORT_VARIABLE_NAME = 'settings_name'`` to your settings.py.
This is useful when some other plugin is already adding ``settings`` to your
template contexts.

See also the bundled
`demo app <https://github.com/jkbrzt/django-settings-export/tree/master/demo>`_.


Development
===========

.. code-block:: bash

    $ cd demo

    # Run demo
    $ python manage.py runserver

    # Run tests on current Python
    $ python manage.py test

    # Run tests on all Pythons
    $ tox

==========
Change Log
==========

See `CHANGELOG <https://github.com/jkbrzt/django-settings-export/blob/master/CHANGELOG.rst>`_.


Licence
=======

BSD. See `LICENCE <https://github.com/jkbrzt/django-settings-export/tree/master/LICENCE>`_ for more details.


Contact
=======


Jakub Roztocil

* https://github.com/jkbrzt
* https://twitter.com/jkbrzt


.. |travis| image:: https://api.travis-ci.org/jkbrzt/django-settings-export.svg
    :target: http://travis-ci.org/jkbrzt/django-settings-export
    :alt: Build Status of the master branch


.. |version| image:: https://badge.fury.io/py/django-settings-export.svg
    :target: https://pypi.python.org/pypi/django-settings-export
    :alt: PyPi

.. |coverage| image:: https://img.shields.io/coveralls/jkbrzt/django-settings-export.svg?branch=master
    :target: https://coveralls.io/r/jkbrzt/django-settings-export?branch=master
    :alt: Coverage
