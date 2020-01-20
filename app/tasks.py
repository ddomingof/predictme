# -*- coding: utf-8 -*-

"""Celery tasks manager."""
from __future__ import absolute_import, unicode_literals

import time

from celery import shared_task


@shared_task
def run_pipeline():
    print('Running pipeline')
    # TODO: Remove
    time.sleep(5)
    print('Done running the pipeline')
