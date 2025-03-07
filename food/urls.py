
"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name='food' # namespaceing the urls

#we are in the /food/urls.py file
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
   # path('<int:item_id>', views.detail, name='detail'),
    path('<int:pk>', views.DetailBasedView.as_view(), name='detail'),
    path('item/', views.item, name='items'),
    path('add', views.CreateItem.as_view(), name='create-item'),
    path('update/<int:item_id>/', views.update_item, name='update-item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete-item'),

    
]
