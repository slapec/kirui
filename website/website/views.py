# coding: utf-8

from pathlib import Path

import sass
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render


def compile_sass(request, path):
    filename = Path(settings.PROJECT_DIR, 'components', path).with_suffix('.scss')
    try:
        filename.resolve()
    except FileNotFoundError:
        raise Http404
    else:
        css = sass.compile(filename=str(filename))
        return HttpResponse(css)


def index(request):
    return render(request, template_name='index.html')
