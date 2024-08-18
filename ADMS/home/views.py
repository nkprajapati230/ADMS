from django.shortcuts import render

def base(request):
    return render(request,'home/base.html')


def home(request):
    return render(request,'home/home.html')


def materials(request):
    return render(request,'home/materials.html')


def contact(request):
    return render(request,'home/contact_us.html')


def about(request):
    return render(request,'home/about_us.html')

