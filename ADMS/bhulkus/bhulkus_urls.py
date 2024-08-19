from django.urls import path
from bhulkus import views


urlpatterns = [
    path('all-bhulku/',views.bhulkus_db,name='bhulkus-db'),
    path('all-bhulku/<str:arg>',views.bhulkus_db,name='bhulkus-db'),
    path('deatiled/<str:id>',views.deatiled,name='detailed-view'),
]
