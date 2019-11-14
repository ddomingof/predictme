# -*- coding: utf-8 -*-

import logging

from django.shortcuts import render
from django.views.decorators.http import require_GET

logger = logging.getLogger(__name__)


@require_GET
def home(request):
    """Render home page."""
    return render(request, 'home.html')


@require_GET
def legal(request):
    """Render imprint page."""
    return render(request, 'legal.html')


@require_GET
def about(request):
    """Render about page."""
    return render(request, 'about.html')
