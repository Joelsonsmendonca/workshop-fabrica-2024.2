from django.contrib import admin
from .models import GitHubUser, GitHubUserDetails  # Certifique-se de importar os modelos corretos

# Registre os modelos no admin
admin.site.register(GitHubUser)
admin.site.register(GitHubUserDetails)