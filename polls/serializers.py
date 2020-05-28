from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from django.contrib.auth.models import User, Group

from rest_framework import routers, serializers, viewsets

from .models import *

# ********************************* serializers.HyperlinkedModelSerializer
# serializers.ModelSerializer
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url','id', 'title', 'descr', 'start_date', 'finish_date' ]



class ActiveQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url','id', 'title', 'descr', 'start_date', 'finish_date' ]

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    #multioption = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Answer
        fields = ['id','url', 'userid',  'question','text', 'option', 'multioption']


class OptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'title'  ]


class MultiOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiOption
        fields = ['url', 'title'  ]
