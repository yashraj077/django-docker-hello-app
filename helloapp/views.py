from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    # only for demo purpose
    return HttpResponse("<center><h1>Built on Django, Deployed using Docker</h1></center>")
