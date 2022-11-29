# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import contact_view, home_view, info_view, loggedin_view, privacy_view, terms_view, info_page_view, info_plant_view

urlpatterns = [
    path('', home_view, name="home"),
    path('terms/', terms_view, name="terms"),
    path('info-page/', info_page_view, name="terms"),
    path('info-plant/', info_plant_view, name="terms"),
    path('privacy/', privacy_view, name="privacy"),
    path('contact/', contact_view, name="contact"),
    path('loggedin/', loggedin_view, name="loggedin"),
    path('info/', info_view, name="info")
]
