from django.contrib import admin
from .models import State, Citizen

# Register your models here.

admin.site.register(Citizen)
admin.site.register(State)
