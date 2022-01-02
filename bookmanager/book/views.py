from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

# route address: /index/
def index(request):
    response = HttpResponse('ok')
    return response