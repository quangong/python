from django.shortcuts import render
from home.models import *
from django.http import HttpResponse

def index(request):
	cat = Category.objects.filter(id = 1)
	print cat
# Create your views here.
