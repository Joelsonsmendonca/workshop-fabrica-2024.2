from django.contrib import admin
from .models import GitHubUser  # Certifique-se de importar o modelo correto

# Registre o modelo GitHubUser no admin
admin.site.register(GitHubUser)