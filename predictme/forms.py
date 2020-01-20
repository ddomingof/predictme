# -*- coding: utf-8 -*-

"""Forms module."""

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


