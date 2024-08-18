from django.urls import path
from home import views

urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home-page'),
    path('materials/',views.materials,name='materials-page'),
    path('contact/',views.contact,name='contact-page'),
    path('about/',views.about,name='about-page'),
]