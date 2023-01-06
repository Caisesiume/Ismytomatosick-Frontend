
# [CODED BY CHRISTOFER & SIMON] Start

from django.urls import path, re_path
from .views import *

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
    path('two-spotted/', two_spotted_view, name="two-spotted spider mites"),
    
    #Result pages
    path('result-bacterial-spot/', result_bacterial_spot_view, name="result bacterial spot"),
    path('result-early-blight/', result_early_blight_view, name="result early blight"),
    path('result-late-blight/', result_late_blight_view, name="result late blight"),
    path('result-leaf-mold/', result_leaf_mold_view, name="result leaf mold"),
    path('result-powdery-mildew/', result_powdery_mildew_view, name="result powdery mildew"),
    path('result-septoria/', result_septoria_view, name="result septoria leaf spot"),
    path('result-target-spot/', result_target_spot_view, name="result target spot"),
    path('result-tomato-mosaic/', result_mosaic_view, name="result tomato mosaic virus"),
    path('result-yellow-curl/', result_yellow_curl_view, name="result tomato yellow leaf curl virus"),
    path('result-two-spotted/', result_two_spotted_view, name="result two-spotted spider mites"),
    path('result-healthy/', result_healthy_view, name="result healthy"),
    path('result-unsure/', result_unsure_view, name="result unsure")
]

# [CODED BY CHRISTOFER & SIMON] End