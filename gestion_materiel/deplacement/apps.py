from django.apps import AppConfig

class DeplacementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deplacement'

    def ready(self):
        import deplacement.signals  # Assurez-vous que le chemin est correct
