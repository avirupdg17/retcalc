from django.shortcuts import render

# Create your views here.
def calcindex(request):
    return render(request,'calcindex.html')