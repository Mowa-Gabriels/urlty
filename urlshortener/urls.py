
from . import views

from django.urls import path

urlpatterns = [
    path('', views.Index, name='index'), 
    path ('url-list/', views.UrlList, name='url-list'),
    path('<str:editable_key>/', views.redirector, name='redirector')
    
]
