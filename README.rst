``django-settings-export``
##########################


|travis| |version|


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


Add ``'django_settings_export.settings_export'`` to
``TEMPLATE_CONTEXT_PROCESSORS`` in your ``settings.py``:

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


Exceptions:

* Listing an undefined setting key in ``SETTINGS_EXPORT`` results in an
  ``UndefinedSettingError``.
* Accessing a unexported setting key on the ``settings`` object in a template
  results in an ``UnexportedSettingError``.


See also the bundled `demo app <demo>`_.

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


Licence
=======

BSD. See `LICENCE <LICENCE>`_ for more details.


Contact
=======


Jakub Roztocil

* https://github.com/jakubroztocil
* https://twitter.com/jakubroztocil


.. |travis| image:: https://api.travis-ci.org/jakubroztocil/django-settings-export.svg
    :target: http://travis-ci.org/jakubroztocil/django-settings-export
    :alt: Build Status of the master branch on Mac/Linux


.. |version| image:: https://badge.fury.io/py/django-settings-export.svg
    :target: https://pypi.python.org/pypi/django-settings-export
