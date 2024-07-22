# deplacement/apps.py
from django.apps import AppConfig

class DeplacementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deplacement'

    def ready(self):
        pass  # Supprimez ou commentez l'importation des signaux
        # import deplacement.signals
