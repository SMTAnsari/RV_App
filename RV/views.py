from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse('Home')


def login_page(request):
    return HttpResponse('login')


def register_page(request):
    return HttpResponse('Register')

