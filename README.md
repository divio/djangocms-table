djangocms-table
===============

A Table Plugin for django CMS.


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`_, run ``pip install djangocms-table``.
* Add ``'djangocms_table'`` to your ``INSTALLED_APPS`` setting.
* If using Django 1.7 add ``'djangocms_table': 'djangocms_table.migrations_django',``to ``MIGRATION_MODULES``  (or define ``MIGRATION_MODULES`` if it does not exists); when django CMS 3.1 will be released, migrations for Django 1.7 will be moved to the standard location and the south-style ones to ``south_migrations``.
* Run ``manage.py migrate djangocms_table``.

Version 1.0.x is compatible with `django CMS` 2.3 and 2.4
Version 1.1.x is compatible with `django CMS` 3.0 only

Do not install version 1.1.x if you are are running `django CMS` 2.3 or 2.4

* In your projects `virtualenv`_, run ``pip install djangocms-table``.
* Add ``'djangocms_table'`` to your ``INSTALLED_APPS`` setting.
* Run ``manage.py migrate cmsplugin_table``.


Kudos
-----

This plugin contains the handsontable.com jquery library.
Thanks to notch-interactive.com as well for some code examples.


Translations
------------

If you want to help translate the plugin please do it on transifex:

https://www.transifex.com/projects/p/django-cms/resource/djangocms-table/

