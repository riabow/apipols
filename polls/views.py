from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *


from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

import datetime
from django.utils import timezone

@csrf_exempt
def activequestions(request):
    if request.method == 'GET':
        Questions = Question.objects.all().filter(finish_date__gte=datetime.date.today() )  #finish_date >= timezone.now)
        serializer = QuestionSerializer(Questions, many=True , context={'request': request} )
        return JsonResponse(serializer.data, safe=False)


def users_answers(request, uid):
    try:
        Answers = Answer.objects.all().filter(userid=uid)
    except Answer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AnswerSerializer(Answers, many=True, context={'request': request} )   # safe=False,
        #return HttpResponse('uid' +str(uid)  )
        return JsonResponse(serializer.data, safe=False )


@csrf_exempt
def polls_list(request):

    """
    List all code   Questions, or create a new Question.
    """
    if request.method == 'GET':
        Questions = Question.objects.all()
        serializer = QuestionSerializer(Questions, many=True , context={'request': request} )
        return JsonResponse(serializer.data, safe=False)
        #return HttpResponse('''<div><center><h1>polls_list </h1><br></div>''')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def polls_detail(request):
    return HttpResponse('''
        <div><center>
        <h1>polls_list </h1>
         <br>
        
        </div>

        ''')