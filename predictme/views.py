# -*- coding: utf-8 -*-

import logging

from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET

from predictme.src.predictme.data_preprocessing import process_data


logger = logging.getLogger(__name__)


@require_GET
def home(request):
    """Render home page."""
    return render(request, 'home.html')


def predict(request):
    """Predict view."""
    if not 'file' in request.FILES:
        return HttpResponseBadRequest(
            'Your genotype file was not found. Please ensure you have submitted a valid file.'
        )

    file = request.FILES['file']
    df = process_data(file)

    print(df)


@require_GET
def legal(request):
    """Render imprint page."""
    return render(request, 'legal.html')


@require_GET
def about(request):
    """Render about page."""
    return render(request, 'about.html')
