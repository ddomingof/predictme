# -*- coding: utf-8 -*-

"""Parsers."""
import logging
import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
application = get_wsgi_application()

from predictme.src.predictme.models import Model

logger = logging.getLogger(__name__)


def delete_database():
    """Delete all objects in the database."""
    logger.info("Deleting database")
    Model.objects.all().delete()
