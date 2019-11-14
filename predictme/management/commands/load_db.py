# -*- coding: utf-8 -*-

"""Command to load the database with app datamodels"""

import logging
import os

from django.core.management.base import BaseCommand

from predictme.src.predictme.constants import (
    RESOURCES_PATH,
)
from predictme.src.predictme.load_db import (
    delete_database,
)


class Command(BaseCommand):
    help = 'Load PredictMe database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--keep-db',
            help='Do not drop DB (--keep-db=True)',
            type=bool
        )

    def handle(self, *args, **options):
        """--keep_db=True avoid dropping the db"""
        logger = logging.getLogger('parser')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(os.path.join(RESOURCES_PATH, 'parser.log'), mode='w')
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)

        # If KEEP DB argument remove
        if not options['keep_db']:
            logger.info('Deleting database')
            delete_database()

        logger.info("")
