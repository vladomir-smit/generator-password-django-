from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random


def home(request: HttpRequest):
    # content = {
    #     'url':
    # }
    return render(request, 'generator/index.html')

def pasword(request: HttpRequest):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvxwz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGIJKLMNOPQRSTUVXWZ')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    length = int(request.GET.get('length', 12))

    for i in range(length):
        thepassword += random.choice(characters)

    content = {
        'thepassword': thepassword
    }
    return render(request, 'generator/password.html', context=content)
