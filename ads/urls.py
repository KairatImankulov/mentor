from django.urls import path
from .views import (
        ads_list, 
        category_list, 
        created_at, 
        update_ad, 
        retrieve_ad,
        delete_ad
)


urlpatterns = [
    path("", ads_list, name="ads_list"),
    path("category", category_list, name="category_list"),    
    path('create', created_at, name="create_at"),
    path('update/<int:pk>/', update_ad, name="update_ad"),
    path('<int:pk>/', retrieve_ad, name='retrieve_ad'),
    path('delete/<int:pk>', delete_ad, name='delete_ad'),
]
