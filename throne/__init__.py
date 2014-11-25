default_app_config = 'throne.ThroneConfig'
from django.apps import AppConfig


class ThroneConfig(AppConfig):
    name = 'throne'
    verbose_name = 'Throne'

    def ready(self):
        import throne.signals
