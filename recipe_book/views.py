import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def service_worker(request):
    response = HttpResponse(
        open(os.path.join(settings.BASE_DIR, "serviceworker.js")).read(),
        content_type="application/javascript",
    )
    return response


def manifest(request):
    return render(
        request,
        "manifest.json",
        {},
        content_type="application/json",
    )


def offline(request):
    return render(request, "offline.html")
