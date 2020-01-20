# -*- coding: utf-8 -*-

"""Data processing module."""

import logging
import re

import gseapy
import pandas as pd
from django.http import HttpResponseBadRequest

from predictme.src.predictme.constants import SNP_COLUMN

logger = logging.getLogger(__name__)


def _read_check(file):
    """Check expression data file."""
    try:
        df = pd.read_csv(file, sep="\t")
    except:
        return HttpResponseBadRequest('There is a problem with your file. Please ensure the file meets the criteria.')

    return df


def _check_genotype_df(df: pd.DataFrame):
    """Check if expression dataFrame is valid."""

    # Check dimensions of expression data dataFrame and ensure it is not empty
    df_shape = df.shape

    if df_shape[0] == 0 or df_shape[1] == 0:
        return HttpResponseBadRequest('You have submitted and empty dataframe')

    # Set the column or raise error
    if SNP_COLUMN in df.columns:
        df.set_index(SNP_COLUMN)
    else:
        return HttpResponseBadRequest('You have submitted and empty dataframe')

    # Check that through the index all the rows have a valid SNP
    SNP_REGEX = re.compile("rs.*", flags=re.IGNORECASE)
    if not all([SNP_REGEX.match(snp) for snp in df.index]):
        return HttpResponseBadRequest('Please ensure that all the SNP row contains valid SNPs [rsXXXXX].')


def process_data(file):
    """Check if expression data file is valid."""
    df = _read_check(file)
    _check_genotype_df(file)

    return df
