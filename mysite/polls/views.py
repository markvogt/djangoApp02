from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# MV: ADD a "route" for HTTP requests for endpoint (URL) named "index"...
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
