from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm, SearchForm
from pprint import pprint
from inspect import getmembers
from django.conf import settings

from django.core.files.storage import FileSystemStorage

from django.core.paginator import Paginator

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(requests):
    #return render(requests, 'articles/index.html', {})
    #redirect('/admin')
    return HttpResponse('''
    <div><center>
    <h1>Тестовое задание </h1>
     <br>
    <a href ="/admin/">admin panel </a><br>
    <a href ="/api/">api </a><br>
    <a href ="/polls/">polls </a><br>
    <a href ="/polls/activequestions">active questions </a><br>
    <a href ="/polls/users_answers/1/"> ответы пользователя id=1 </a><br>
    </div>
    
    ''')

