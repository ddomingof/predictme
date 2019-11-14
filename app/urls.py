# -*- coding: utf-8 -*-

"""Urls."""
from django.contrib import admin
from django.urls import path

from predictme.views import (
    about,
    home,
    legal,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about', about, name='about'),
    path('legal', legal, name='legal'),
]
