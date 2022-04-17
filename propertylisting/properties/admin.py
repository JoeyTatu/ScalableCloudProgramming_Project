# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
#from import_export.admin import ImportExportMixin
from .models import Property    # Register your models here.


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('listing_type','ber_rating','county')

admin.site.register(Property,PropertyAdmin)

