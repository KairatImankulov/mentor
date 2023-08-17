from django.urls import path
from .views import ads_list

urlpatterns = [
    path("", ads_list)
    
]
