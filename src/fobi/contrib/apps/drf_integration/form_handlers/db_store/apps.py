__title__ = 'fobi.contrib.apps.drf_integration.form_handlers.db_store.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

try:
    __all__ = ('Config',)

    from django.apps import AppConfig

    class Config(AppConfig):
        """Config."""

        name = 'fobi.contrib.apps.drf_integration.form_handlers.db_store'
        label = 'fobi_contrib_apps_drf_integration_form_handlers_db_store'

except ImportError:
    pass