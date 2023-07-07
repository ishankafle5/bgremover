from django.shortcuts import render

# Create your views here.

def gotohome(request):
    return render(request,'index.html')

def removebgpage(request):
    return render(request,'bgremove.html')