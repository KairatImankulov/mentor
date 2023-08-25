from typing import Any, Dict
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib import messages

from users.models import User

from django.urls import reverse, reverse_lazy
from .models import Ads, Category
from .forms import AdForm
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView


def category_list (request):
    all_categoryes = Ads.objects.all()
    
    context = {
        "all_categoryes": all_categoryes
    }
    return render(request, 'category.html', context=context)


class AdsListView(ListView):
    template_name = 'index.html'
    queryset = Ads.objects.all()
    context_object_name = 'all_ads'
    
    # def get(self, request, *args, **kwargs):
    #     all_ads = Ads.objects.all()
    #     return render(request, self.template_name, {'all_ads': all_ads})


    # all_ads = Ads.objects.filter(created_at__lte=timezone.now())
    # all_ads = Ads.objects.filter(title__icontains="Test")
    # all_ads = Ads.objects.filter(owner__isnull=True)
    # all_ads = Ads.objects.filter(description__icontains="s", created_at__year=2023)
    # admin = User.objects.get(username='admin')
    # all_ads = Ads.objects.filter(owner=admin)
    # all_ads = Ads.objects.filter(price__in=[200, 3000, 343, 2500])


class AdsCreateView(CreateView):
    template_name = 'create_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads_list')

    # if request.method == 'POST':
    #     form = AdForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('ads_list')
    # else:
    #     form_of_ad = AdForm()
    # return render(request, 'create_ad.html',{'form_of_ad':form_of_ad})


class AdsDeleteView(DeleteView):
    queryset = Ads.objects.all()
    template_name = 'delete_ad.html'
    success_url = reverse_lazy('ads_list')


class AdsUpdateView(UpdateView):
    template_name = 'update_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads_list')
    

    # if request.method == 'POST' or request.method == 'PATCH':
    #     form = AdForm(request.POST, request.FILES, instance=ad)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse ('<h1> Success edited </h1>')
    #     else:
    #         return HttpResponse ('<h1> Error edited </h1>')
    # else:
    #     form_of_ad = AdForm(instance=ad)
    #     return render(request, 'update_ad.html', {'form_of_ad':form_of_ad})


class AdsDetailView(DetailView):
    template_name = 'retrieve_ad.html'
    queryset = Ads.objects.all()
    context_object_name = 'ad'


# def delete_ad(request, pk):
#     ad = Ads.objects.get(id=pk)
#     ad.delete()
#     messages.success(request, 'Обьект успешно удален')
#     return redirect('ads_list')