"""apipols URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from django.contrib.auth.models import User, Group

from rest_framework import routers, serializers, viewsets

from polls.models import *
from . import views

import datetime
from django.utils import timezone

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()





# *********************************
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url','id', 'title', 'descr', 'start_date', 'finish_date' ]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

router.register(r'Question', QuestionViewSet)

class ActiveQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['url','id', 'title', 'descr', 'start_date', 'finish_date' ]

class ActiveQuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().filter(finish_date__gte=datetime.date.today() )  #finish_date >= timezone.now)
    serializer_class = ActiveQuestionSerializer

router.register(r'ActiveQuestion', ActiveQuestionViewSet)


# *********************************
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    #multioption = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Answer
        fields = ['id','url', 'userid', 'text', 'question', 'option', 'multioption']

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

router.register(r'Answer', AnswerViewSet)
# *********************************
class OptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Option
        fields = ['id', 'title'  ]

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

router.register(r'Option', OptionViewSet)

# *********************************
class MultiOptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MultiOption
        fields = ['url', 'title'  ]

class MultiOptionViewSet(viewsets.ModelViewSet):
    queryset = MultiOption.objects.all()
    serializer_class = MultiOptionSerializer

router.register(r'MultiOption', MultiOptionViewSet)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),

]
