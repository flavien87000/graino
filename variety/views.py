from django.shortcuts import render, HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms
from django.utils.text import slugify

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import Group

from variety.models import Variety, Category

# Variety view


def update(request):
    for o in Category.objects.all():
        o.url = slugify(o.title)
        o.save()