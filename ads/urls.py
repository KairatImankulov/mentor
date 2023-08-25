from django.urls import path
from .views import (
        AdsListView,
        category_list, 
        AdsCreateView, 
        AdsUpdateView, 
        AdsDetailView,
        AdsDeleteView,
)


urlpatterns = [
    path("", AdsListView.as_view(), name="ads_list"),
    path("category", category_list, name="category_list"),    
    path('create', AdsCreateView.as_view(), name="create_at"),
    path('update/<int:pk>/', AdsUpdateView.as_view(), name="update_ad"),
    path('<int:pk>/', AdsDetailView.as_view(), name='retrieve_ad'),
    path('delete/<int:pk>', AdsDeleteView.as_view(), name='delete_ad'),
]
