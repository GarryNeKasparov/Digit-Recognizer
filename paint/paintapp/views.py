from django.shortcuts import render
from .models import MyModel
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def paint(request):
    if request.method == "GET":
        pass