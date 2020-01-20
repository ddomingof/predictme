# -*- coding: utf-8 -*-

"""Forms module."""

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'box__file'
            visible.field.widget.attrs['id'] = 'file'