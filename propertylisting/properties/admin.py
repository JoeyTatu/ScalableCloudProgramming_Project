# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('listing_type','ber_rating','county')

admin.site.register(Property)

