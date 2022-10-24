from multiprocessing.util import get_temp_dir
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template

def index(request):
    index_html = loader.get_template('/home/urmil/Desktop/My_Profile/UK_Profile/members/templates/assets/index.html')
    return HttpResponse(index_html.render())
# Create your views here.
