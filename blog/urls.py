# blog app에서 사용할 url을 등록
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]