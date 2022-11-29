# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

def home_view(request):
    return render(request, "home/home.html")

def info_view(request):
    return render(request, "home/info.html")

def info_page_view(request):
    return render(request, "home/info-page.html")

def info_plant_view(request):
    return render(request, "home/info-plant.html")

def contact_view(request):
    return render(request, "home/contact.html")

def terms_view(request):
    return render(request, "home/terms.html")

def privacy_view(request):
    return render(request, "home/privacy.html")

def loggedin_view(request):
    return render(request, "home/loggedin.html")
