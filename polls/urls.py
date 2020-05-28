from django.urls import path
from . import views

urlpatterns = [
    path('', views.polls_list),
    path('activequestions', views.activequestions ),
    path('users_answers/<int:uid>/', views.users_answers),
]