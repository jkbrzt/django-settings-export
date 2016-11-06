==========
Change Log
==========

This document records all notable changes to
`django-settings-export <https://github.com/jkbrzt/django-settings-export>`_.
This project adheres to `Semantic Versioning <http://semver.org/>`_.


1.2.1 (2016-11-06)
------------------

* The exported ``settings`` object is now an instance of ``dict`` subclass
  to allow iteration, etc.



1.1.0 (2016-03-10)
------------------

* Added ability to set the name of the context variable to something besides
  ``settings`` via ``SETTINGS_EXPORT_VARIABLE_NAME``.
