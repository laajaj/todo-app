
from django.contrib import admin
from .models import Task

# Enregistrer le modèle Task dans l'admin
admin.site.register(Task)