from django.apps import AppConfig


class StreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stream'

    def ready(self):
        import stream.signals


class AccountsConfig(AppConfig):
    name = 'stream'
    # This function is the only new thing in this file
    # it just imports the signal file when the app is ready
    def ready(self):
        import stream.signals