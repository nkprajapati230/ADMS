from django.urls import path
from leaders import views

urlpatterns = [
    path('',views.leaders_view,name='leaders-page'),
    path('login/',views.login_view,name='login-page'),
] 
