# blog app에서 사용할 url을 등록
from django.urls import path
from . import views

urlpatterns = [
    # <ip : port>/blog : 블로그 메인 페이지
    path('', views.index),
    # <ip : port>/blog/글번호(pk)
    # /blog/1234 -> 1234를 숫자가 아닌 문자열 '1234'로 인식
    # path('<int:pk>/'),
    path('<int:pk>/', views.single_post_page)
]
