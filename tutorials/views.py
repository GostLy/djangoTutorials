# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world, I'm your wild girl. \
                        Ch-Ch-Ch-CHERRY-BOMB")
