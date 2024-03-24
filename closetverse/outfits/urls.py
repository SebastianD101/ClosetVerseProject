from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # URLs for Shirts
    path('shirts/', views.list_shirts, name='list_shirts'),
    path('shirts/add/', views.add_shirt, name='add_shirt'),
    path('shirts/edit/<int:pk>/', views.edit_shirt, name='edit_shirt'),
    path('shirts/delete/<int:pk>/', views.delete_shirt, name='delete_shirt'),

    # URLs for Pants
    path('pants/', views.list_pants, name='list_pants'),
    path('pants/add/', views.add_pants, name='add_pants'),
    path('pants/edit/<int:pk>/', views.edit_pants, name='edit_pants'),
    path('pants/delete/<int:pk>/', views.delete_pants, name='delete_pants'),

    # URLs for Shoes
    path('shoes/', views.list_shoes, name='list_shoes'),
    path('shoes/add/', views.add_shoes, name='add_shoes'),
    path('shoes/edit/<int:pk>/', views.edit_shoes, name='edit_shoes'),
    path('shoes/delete/<int:pk>/', views.delete_shoes, name='delete_shoes'),

    # URLs for Jackets
    path('jackets/', views.list_jackets, name='list_jackets'),
    path('jackets/add/', views.add_jacket, name='add_jacket'),
    path('jackets/edit/<int:pk>/', views.edit_jacket, name='edit_jacket'),
    path('jackets/delete/<int:pk>/', views.delete_jacket, name='delete_jacket'),

    # URLs for Accessories
    path('accessories/', views.list_accessories, name='list_accessories'),
    path('accessories/add/', views.add_accessories, name='add_accessories'),
    path('accessories/edit/<int:pk>/', views.edit_accessories, name='edit_accessories'),
    path('accessories/delete/<int:pk>/', views.delete_accessories, name='delete_accessories'),

    # URLs for Outfits
    path('outfits/', views.list_outfits, name='list_outfits'),
    path('outfits/add/', views.add_outfit, name='add_outfit'),
    path('outfits/edit/<int:pk>/', views.edit_outfit, name='edit_outfit'),
    path('outfits/delete/<int:pk>/', views.delete_outfit, name='delete_outfit'),
]