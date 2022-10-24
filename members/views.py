from multiprocessing.util import get_temp_dir
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template
from UK_Profile.settings import TEMPLATE_DIRS

def index(request):
    index_html = loader.get_template(TEMPLATE_DIRS+'/index.html')
    return HttpResponse(index_html.render())
# Create your views here.
