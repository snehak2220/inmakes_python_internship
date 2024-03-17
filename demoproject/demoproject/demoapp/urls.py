from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='about'),
    path('detail/',views.detail,name='detail'),
    path('thanks/',views.thanks,name='thanks'),
    path('calculate/',views.calculate,name='calculate')


]