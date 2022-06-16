from django.shortcuts import render
from .models import Item
from django.http import HttpResponse #used for testing
from django.shortcuts import render #throws on your web page
# Create your views here.

def index(request):
    return HttpResponse('This function is running')
