from django.shortcuts import render,redirect
from home import views as vw
from bhulkus.models import bhulku
import random


def bhulkus_db(request,arg=None):
    if arg=='status':
        return redirect(vw.home)
    for i in range(60):
        b=bhulku()
        try:
            b.id=random.randint(1,41)
        except:
            continue
        b.first_name='Test'
        b.last_name='Test'
        b.address='Test'
        b.phone_number=random.randint(9000000000,9999999999)
        b.age=random.randint(8,20)
        b.standard=random.randint(2,10)
        b.save()
    user=bhulku.objects.all()        
    return render(request,'bhulkus/bhulkus_db.html',{'bhulku':user})





def detailed(request,id):
    b=bhulku.objects.all(id=id)
    return render(request,'bhulkus/detailed.html',{'bhulku':b})