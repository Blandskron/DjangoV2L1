from django.urls import path
from . import views

urlpatterns = [
    path('manage-data/', views.manage_data, name='manage_data'), 
    path('add-author/', views.add_author, name='add_author'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('add-entry/', views.add_entry, name='add_entry'),
    path('success/', views.success_page, name='success_page'),
]
