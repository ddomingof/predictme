# -*- coding: utf-8 -*-

import logging

from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from app.tasks import run_pipeline

from predictme.src.predictme.constants import EMAIL_CONTENT, EMAIL_SUBJECT
from predictme.src.predictme.data_preprocessing import process_data
from .forms import UploadFileForm

logger = logging.getLogger(__name__)

from django.core.mail import send_mail


@require_GET
def home(request):
    """Render home page."""
    return render(request, "home.html", {"form": UploadFileForm()})


def predict(request):
    """Predict view."""
    form = UploadFileForm(request.POST, request.FILES)

    # Check if form is valid
    if not form.is_valid():
        return HttpResponseBadRequest(
            'There was a problem with the submitted form. Please ensure you have submitted a valid file.'
        )

    df = process_data(request.FILES['file'])

    if isinstance(df, str):  # df would be the message to the user
        return HttpResponseBadRequest(df)

    # Run celery task
    run_pipeline()

    send_mail(
        EMAIL_SUBJECT,
        EMAIL_CONTENT,
        f'daniel.domingo.fernandez@scai.fraunhofer.de',
        ['ddomingof@yahoo.es'],
        fail_silently=False,
    )

    return HttpResponse("Success")


@require_GET
def legal(request):
    """Render imprint page."""
    return render(request, 'legal.html')


@require_GET
def about(request):
    """Render about page."""
    return render(request, 'about.html')
