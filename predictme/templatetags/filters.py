# -*- coding: utf-8 -*-

"""Filters."""

from django.template.defaulttags import register


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_integer(dictionary, key):
    return int(dictionary.get(key))
