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

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
router.register(r'users', UserViewSet)
#************************
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

router.register(r'group', GroupViewSet)




# *********************************
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    #answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #start_date = serializers.DateTimeField(read_only=True)
    #print(start_date)
    class Meta:
        model = Question
        fields = ['url','id', 'title', 'descr', 'start_date', 'finish_date' ]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

router.register(r'Question', QuestionViewSet)


# *********************************
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    multioption = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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



#router.register(r'groups', views.GroupViewSet)
#router.register(r'part', views.PartViewSet)
#router.register(r'Brent', views.BrentViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),

]
