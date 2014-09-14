``django-settings-export``
##########################

Often it is needed to make some of your Django project's settings
accessible from within templates. This app provides a simple mechanism
for doing just that.

It tries to make settings management easier by:

* Requiring you to be explicit about what
  settings should be exported to templates.
* Failing loudly if an undefined or unexported setting is accessed.


Installation
============


.. code-block:: bash

    $ pip install django-settings-export


Add ``'django_settings_export.export_settings'`` to
``TEMPLATE_CONTEXT_PROCESSORS`` in your ``settings.py``:

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = [
        # [...]
        'django_settings_export.export_settings',
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


Exceptions:

* Listing an undefined setting key in ``SETTINGS_EXPORT`` results in an
  ``UndefinedSettingError``.
* Accessing a unexported setting key on the ``settings`` object in a template
  results in an ``UnexportedSettingError``.


Development
===========


Run tests:

.. code-block:: bash

    $ cd demo
    $ python manage.py test


Licence
=======

BSD. See `LICENCE <LICENCE>`_ for more details.


Contact
=======


Jakub Roztočil

* https://github.com/jakubroztocil
* https://twitter.com/jakubroztocil

