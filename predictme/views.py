# -*- coding: utf-8 -*-

import logging

from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET

from predictme.src.predictme.constants import (
    ADPD_AUTOENCODER_MODEL,
    AUTOENCODER_TRAINED_MATRIX,
    TRAINED_PATIENT_CLUSTERS,
    SUBGRAPH_15_RDATA,
)
from predictme.src.predictme.data_preprocessing import process_data
from .forms import UploadFileForm
from .src.predictme.R import run_r

logger = logging.getLogger(__name__)


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

    # Transpose matrix (patients (rows) x snps (columns))
    df = df.T

    # Evaluate test data with our classifier
    predictions = run_r(
        user_df=df,
        **{'autoencoder': ADPD_AUTOENCODER_MODEL,
           'autoencoder_trainer_matrix': AUTOENCODER_TRAINED_MATRIX,
           'subgraph_15_rdata': SUBGRAPH_15_RDATA,
           'trained_patient_clusters': TRAINED_PATIENT_CLUSTERS
           }
    )

    return render(request, 'results.html', context={'predictions': 'predictions'})


@require_GET
def legal(request):
    """Render imprint page."""
    return render(request, 'legal.html')


@require_GET
def about(request):
    """Render about page."""
    return render(request, 'about.html')
