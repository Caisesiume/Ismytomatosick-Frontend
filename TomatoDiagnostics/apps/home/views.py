# [CODED BY CHRISTOFER & SIMON] Start

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


#Plant pages

def bacterial_spot_view(request):
    return render(request, "home/bacterial-spot.html")

def early_blight_view(request):
    return render(request, "home/early-blight.html")

def late_blight_view(request):
    return render(request, "home/late-blight.html")

def leaf_mold_view(request):
    return render(request, "home/leaf-mold.html")

def powdery_mildew_view(request):
    return render(request, "home/powdery-mildew.html")

def septoria_view(request):
    return render(request, "home/septoria-leaf-spot.html")

def target_spot_view(request):
    return render(request, "home/target-spot.html")

def mosaic_view(request):
    return render(request, "home/tomato-mosaic-virus.html")

def yellow_curl_view(request):
    return render(request, "home/tomato-yellow-curl-virus.html")

def two_spotted_view(request):
    return render(request, "home/two-spotted-spider-mites.html")

#Result pages

def result_bacterial_spot_view(request):
    return render(request, "home/result-bacterial-spot.html")

def result_early_blight_view(request):
    return render(request, "home/result-early-blight.html")

def result_late_blight_view(request):
    return render(request, "home/result-late-blight.html")

def result_leaf_mold_view(request):
    return render(request, "home/result-leaf-mold.html")

def result_powdery_mildew_view(request):
    return render(request, "home/result-powdery-mildew.html")

def result_septoria_view(request):
    return render(request, "home/result-septoria-leaf-spot.html")

def result_target_spot_view(request):
    return render(request, "home/result-target-spot.html")

def result_mosaic_view(request):
    return render(request, "home/result-tomato-mosaic-virus.html")

def result_yellow_curl_view(request):
    return render(request, "home/result-tomato-yellow-curl-virus.html")

def result_two_spotted_view(request):
    return render(request, "home/result-two-spotted-spider-mites.html")




# [CODED BY CHRISTOFER & SIMON] End