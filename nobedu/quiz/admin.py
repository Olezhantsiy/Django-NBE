from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import *

# Register your models here.
@register(QuesModel)
class QuesModelAdmin(ModelAdmin):
    list_display = ("question", "typeq")


