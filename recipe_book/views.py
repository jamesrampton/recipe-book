import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def manifest(request):
    return render(
        request,
        "manifest.json",
        {},
        content_type="application/json",
    )
