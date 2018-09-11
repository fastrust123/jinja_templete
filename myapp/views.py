import os
import time


from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.template import Context, loader
from jinja2 import Environment, FileSystemLoader
from itertools import chain


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESS_TIME = 5


def index(request):

    return render(request, 'jinja2/index.html')

def simple_ad_add_official(request):

    return render(request, 'jinja2/ad-add-official.html')

def simple_ad_add_organisation(request):

    return render(request, 'jinja2/ad-add-organisation.html')

def simple_ad_ap_revise_user(request):

    return render(request, 'jinja2/ad-ap-revise-user.html')

def simple_ad_change_password(request):

    return render(request, 'jinja2/ad-change-password.html')