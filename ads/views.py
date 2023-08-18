from django.shortcuts import render
from django.http import HttpResponse

from .models import Ads

def ads_list (request):
    all_ads = Ads.objects.all()
    
    context = {
        "all_ads": all_ads
    }
    return render(request, 'index.html', context=context)
