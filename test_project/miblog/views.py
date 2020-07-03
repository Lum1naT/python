from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

def index(response):
    response = "You're looking at index of miblog."
    return HttpResponse(response)

# DO MORE VIEWS
