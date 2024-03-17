from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return HttpResponse('This is the about page')
def contact(request):
    return render(request,'contact.html')
def detail(request):
    return render(request,'detail.html')
def thanks(request):
    return HttpResponse("THANKS")
def calculate(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    mul=x*y
    sub=x-y
    div=x/y
    return render(request,'result.html',{'addition':add,'subtraction':sub,'multiplication':mul,'division':div})



