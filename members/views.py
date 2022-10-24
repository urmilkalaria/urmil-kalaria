from multiprocessing.util import get_temp_dir
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template
from UK_Profile.settings import BASE_DIR
import os
def index(request):
    path = os.path.join(BASE_DIR, 'members/templates/assets/index.html')
    index_html = loader.get_template(path)
    return HttpResponse(index_html.render())
# Create your views here.
