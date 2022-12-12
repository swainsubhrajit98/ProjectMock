from django.shortcuts import render

# Create your views here.
def Mock(request):
    return render(request,'Mock.html')