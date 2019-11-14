# -*- coding: utf-8 -*-

"""This module contains all the database manager definitions for the admin"""

from django.contrib import admin

from predictme.src.predictme.models import Model


class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'blob',)
    ordering = ('id',)
    search_fields = ('id',)


admin.site.register(Model, ModelAdmin)
