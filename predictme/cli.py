# -*- coding: utf-8 -*-

"""Command line interface."""

import logging

import click

log = logging.getLogger(__name__)


@click.group(help='PredictMe Web App')
def main():
    """PredictMe."""
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
