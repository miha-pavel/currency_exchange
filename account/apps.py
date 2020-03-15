from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):
        # Импорт делаеться только здесь
        import account.signals
