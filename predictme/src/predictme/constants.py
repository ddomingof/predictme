# -*- coding: utf-8 -*-

"""Constants."""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Project path
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))

# Resources path
RESOURCES_DIR = os.path.join(PROJECT_DIR, 'data')

"""Static Files"""
### Our AD PD based training data
SUBGRAPH_15_RDATA = os.path.join(RESOURCES_DIR, 'subgraph15_snpset148.RData')
ADPD_AUTOENCODER_MODEL = os.path.join(RESOURCES_DIR, 'models/')
AUTOENCODER_TRAINED_MATRIX = os.path.join(RESOURCES_DIR, "autoencoder_trained_matrix.RData")
TRAINED_PATIENT_CLUSTERS = os.path.join(RESOURCES_DIR, "trained_patient_clusters.RData")

CLEANME_DIRECTORY = os.path.join(RESOURCES_DIR, "classifier_model")

## USER Data
USER_FILE = os.path.join(RESOURCES_DIR, 'Asif_Genotype_Disease_Only_ROSMAP.csv')
OUTPUT_FILE = os.path.join(RESOURCES_DIR, "patient_clusters.csv")

"""Dataframe Constants"""

SNP_COLUMN = "SNP"
