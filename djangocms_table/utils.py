import django
import os
from distutils.version import LooseVersion
from django.utils.functional import LazyObject
from django.core.files.storage import get_storage_class


#The following class is taken from https://github.com/jezdez/django/compare/feature/staticfiles-templatetag
#and should be removed and replaced by the django-core version in 1.4

default_storage = 'django.contrib.staticfiles.storage.StaticFilesStorage'
if LooseVersion(django.get_version()) < LooseVersion('1.3'):
    default_storage = 'staticfiles.storage.StaticFilesStorage'


class ConfiguredStorage(LazyObject):
    def _setup(self):
        from django.conf import settings
        self._wrapped = get_storage_class(getattr(settings, 'STATICFILES_STORAGE', default_storage))()

configured_storage = ConfiguredStorage()

def static_url(path):
    '''
    Helper that prefixes a URL with STATIC_URL and cms
    '''
    if not path:
        return ''
    return configured_storage.url(os.path.join('table', path))
