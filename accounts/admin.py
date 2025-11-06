from django.contrib import admin

# Registering models here.
from .models import Profile

admin.site.register(Profile)