from django.apps import AppConfig


class PortafoleoConfig(AppConfig):
    name = 'portafoleo'

    def ready(self):
        import portafoleo.signals
