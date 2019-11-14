# -*- coding: utf-8 -*-

"""Model definitions."""

from django.db import models
from picklefield.fields import PickledObjectField


class Model(models.Model):
    """GLM model."""
    blob = PickledObjectField()

    def __str__(self):
        return f'Hello, I am the GLM model #{self.id}'
