from django.apps import AppConfig


class HomeConfig(AppConfig):
    name = 'apps.home'

    def ready(self):
        import apps.home.signals
