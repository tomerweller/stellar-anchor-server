"""This module defines the URL patterns for the `/.well-known/stellar.toml` endpoint."""
from django.urls import path
from .views import generate_toml

urlpatterns = [path("stellar.toml", generate_toml)]
