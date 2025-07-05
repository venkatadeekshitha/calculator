from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.


def home(request):
    result=None
    if request.method=='POST':
      try:
            a=(int)(request.POST.get("num1"))
            b=(int)(request.POST.get("num2"))
            o=request.POST.get('op')
            if(o=='add'):
               result=a+b
               return redirect('hello',result=result)
         #return HttpResponse(request,'index1.html',{'result':10})
      except(ValueError,TypeError):
         result="Invalid"


      
      
       
    return render(request,'home.html',{'result':result})

def hello(request,result):
      return render(request,'result.html', {'result':result})