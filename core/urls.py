from django.urls import path
from . import views

urlpatterns = [
    path('github_user/', views.github_user, name='github_user'),
]