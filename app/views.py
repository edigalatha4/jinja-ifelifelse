from django.shortcuts import render

# Create your views here.
def latha(request):
    d={'a':20,'b':50,'c':10}
    return render(request,'if-elif-else.html',d)
