from django.shortcuts import render,redirect
from home import views as vw
from bhulkus.models import bhulku
import random


status=False
def bhulkus_db(request,arg=None):
    global status
    if arg=='status':
        if status==True:
            status=False
        else:
            status=True
    # for i in range(60):
    #     b=bhulku()
    #     try:
    #         b.id=random.randint(2,41)
    #     except:
    #         continue
    #     b.first_name='Test'
    #     b.last_name='Test'
    #     b.address='Test'
    #     b.phone_number=random.randint(9000000000,9999999999)
    #     b.age=random.randint(8,20)
    #     b.standard=random.randint(2,10)
    #     b.save()
    user=bhulku.objects.all()        
    return render(request,'bhulkus/bhulkus_db.html',{'bhulku':user,'status':status})





def detailed(request,id):
    user=bhulku.objects.filter(id=id).first()
    return render(request,'bhulkus/detailed.html',{'bhulku':user})