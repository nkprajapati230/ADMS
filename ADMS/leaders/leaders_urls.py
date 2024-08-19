from django.urls import path
from leaders import views

urlpatterns = [
    path('login/',views.login_view,name='login-page'),
] 
