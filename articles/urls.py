from django.urls import path, include  # 반드시 추가해줘야 함
from . import views  # 같은 articles 내 view 를 가져옴


# /articles/ ____ , 사용자는 이미 articles 까지 들어온 상태
urlpatterns = [
    path('', views.index),
    path('<int:article_pk>/', views.detail),

    path('new/', views.new),  # views 의 new함수, new.html 생성 필요
    path('create/', views.create),
    # /articles/4/delete/
    path('<int:article_pk>/delete/', views.delete),
]