from django.urls import path
from home import views

urlpatterns = [
    path('',views.base,name='base') 
]
