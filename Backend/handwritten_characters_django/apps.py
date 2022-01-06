from django.apps import AppConfig


class InitialConfig(AppConfig):
    name = 'handwritten_characters_django'
    verbose_name = "Characters Recognition"

    def ready(self):
        print("Config working")