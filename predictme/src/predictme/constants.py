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
GENOTYPE_DATA = os.path.join(RESOURCES_DIR, 'Asif_Genotype_Disease_Only_ROSMAP.csv')
SUGBRAPH_SNPS = os.path.join(RESOURCES_DIR, 'subgraphs15_snps_mod1.csv')
SUBGRAPH_15_RDATA = os.path.join(RESOURCES_DIR, 'subgraph15_snpset148.RData')

INPUT_FOR_MODEL = os.path.join(RESOURCES_DIR, "rosmap148.snp.mat.RData")

"""Dataframe Constants"""

SNP_COLUMN = "SNP"
