
# [CODED BY CHRISTOFER & SIMON] Start

from django.urls import path, re_path
from .views import contact_view, home_view, info_view, loggedin_view, privacy_view, terms_view, info_page_view, info_plant_view, bacterial_spot_view, early_blight_view, late_blight_view, leaf_mold_view, powdery_mildew_view, septoria_view, target_spot_view, mosaic_view, yellow_curl_view, two_spotted_view

urlpatterns = [
    path('', home_view, name="home"),
    path('terms/', terms_view, name="terms"),
    path('info-page/', info_page_view, name="info-page"),
    path('info-plant/', info_plant_view, name="info-plant"),
    path('privacy/', privacy_view, name="privacy"),
    path('contact/', contact_view, name="contact"),
    path('loggedin/', loggedin_view, name="loggedin"),
    path('info/', info_view, name="info"),
    
    #Plant pages
    path('bacterial-spot/', bacterial_spot_view, name="bacterial spot"),
    path('early-blight/', early_blight_view, name="early blight"),
    path('late-blight/', late_blight_view, name="late blight"),
    path('leaf-mold/', leaf_mold_view, name="leaf mold"),
    path('powdery-mildew/', powdery_mildew_view, name="powdery mildew"),
    path('septoria/', septoria_view, name="septoria leaf spot"),
    path('target-spot/', target_spot_view, name="target spot"),
    path('mosaic/', mosaic_view, name="tomato mosaic virus"),
    path('yellow-curl/', yellow_curl_view, name="tomato yellow leaf curl virus"),
    path('two-spotted/', two_spotted_view, name="two-spotted spider mites")
    
]

# [CODED BY CHRISTOFER & SIMON] End