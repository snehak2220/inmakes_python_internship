from django.http import HttpResponse
from django.shortcuts import render
from .models import Places
from .models import Team

# Create your views here.
def demo(request):
    obj=Places.objects.all()
    obj2=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})
#def about(request):
   # return render(request,"about.html")
#def contact(request):
   # return HttpResponse("This is my contact page")
