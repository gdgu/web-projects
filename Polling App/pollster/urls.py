from django.urls import path
from . import views

app_name = 'pollster'
urlpatterns = [
    path('', views.poll,name="poll"),
    path('choice/<int:question_id>',views.choice,name="choice"),
    path('result/<int:question_id>',views.result,name="result"),

]