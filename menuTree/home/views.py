from django.shortcuts import render
from django.http import HttpResponse
from .models import Catagory
# Create your views here.
def index(request):
    listCatagory = Catagory.objects.all()
    return render(request, 'home/index.html', {'listCatagory': listCatagory})