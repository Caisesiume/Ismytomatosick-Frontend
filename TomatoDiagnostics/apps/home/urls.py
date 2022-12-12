
# [CODED BY CHRISTOFER & SIMON] Start

from django.urls import path, re_path
from .views import contact_view, home_view, info_view, loggedin_view, privacy_view, result_bacterial_spot_view, result_early_blight_view, result_healthy_view, result_late_blight_view, result_leaf_mold_view, result_mosaic_view, result_powdery_mildew_view, result_septoria_view, result_target_spot_view, result_two_spotted_view, result_yellow_curl_view, terms_view, info_page_view, info_plant_view, bacterial_spot_view, early_blight_view, late_blight_view, leaf_mold_view, powdery_mildew_view, septoria_view, target_spot_view, mosaic_view, yellow_curl_view, two_spotted_view

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
    path('result-bacterial-spot/', result_bacterial_spot_view, name="result bacterial spot"),
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
    path('result-mosaic/', result_mosaic_view, name="result tomato mosaic virus"),
    path('result-yellow-curl/', result_yellow_curl_view, name="result tomato yellow leaf curl virus"),
    path('result-two-spotted/', result_two_spotted_view, name="result two-spotted spider mites"),
    path('result-healthy/', result_healthy_view, name="result healthy")
    
]

# [CODED BY CHRISTOFER & SIMON] End