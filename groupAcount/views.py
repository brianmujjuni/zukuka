from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'groupAccount/index.html')

def add_group(request):
    return render(request,'groupAccount/Index.html')