from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person

# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_field = ("description",)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("lastname", "firstname", "height", "weight")
    search_field = ("lastname", "firstname", "height", "weight")



