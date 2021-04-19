from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remdesivir', views.rem, name='rem'),
    path('bed', views.bed, name='bed'),
    path('oxygen', views.oxygen, name='oxygen'),
    path('plasma', views.plasma, name='plasma'),
    path('add', views.addNew, name='add'),
    path('contact', views.contact, name='contact'),
    
]
