from django.shortcuts import render,redirect
from home import views as vw
from bhulkus.models import bhulku
import random


def bhulkus_db(request,arg=None):
    status=False
    if arg:
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


def delete(request,id):
    user=bhulku.objects.filter(id=id).first()
    user.delete()
    return redirect('bhulkus-db')



def update(request,id):
    if request.method=='POST':
        f_name=request.POST.get('first_name')
        m_name=request.POST.get('middle_name')
        l_name=request.POST.get('last_name')
        std=request.POST.get('standard')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        sch=request.POST.get('school')
        number=request.POST.get('phone_number')
        add=request.POST.get('address')
        reg=request.POST.get('regular')
        if reg==None:
            reg=False
        else:
            reg=True

        user=bhulku.objects.filter(id=id).first()

        user.first_name=f_name
        user.middle_name=m_name
        user.last_name=l_name

        user.standard=std
        user.dob=dob
        user.age=age
        
        user.school=sch
        user.phone_number=number
        user.address=add
        user.regular=reg

        user.save()
    return redirect('/bhulkus/detailed/'+str(user.id))


