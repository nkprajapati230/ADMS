from django.urls import path
from bhulkus import views


urlpatterns = [
    path('all-bhulku/',views.bhulkus_db,name='bhulkus-db'),
    path('all-bhulku/<str:arg>',views.bhulkus_db,name='bhulkus-db'),
    path('detailed/<int:id>',views.detailed,name='detailed-view'),
    path('delete/<int:id>',views.delete,name='delete-db'),
    path('update/<int:id>',views.update,name='update-db')
]
