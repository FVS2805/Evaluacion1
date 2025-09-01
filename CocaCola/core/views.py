from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"core/home.html")

def QuienesSomos(request):
    return render(request,"core/QuienSomos.html")

def faq(request):
    return render(request,"core/FAQ.html")

def Galeria(request):
    return render(request,"core/Galeria.html")
