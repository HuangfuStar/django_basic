from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

# route address: /index/
def index(request):

    response = render(request, 'book/index.html')
    return response