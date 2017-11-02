import sass
from django.http import HttpResponse
from django.shortcuts import render


def kirui_css(request):
    css = sass.compile(filename='/home/lovasb/WORK/kirui/components/bundle.scss')
    return HttpResponse(css)


def index(request):
    return render(request, template_name='index.html')
