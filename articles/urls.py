from django.urls import path, include  # 반드시 추가해줘야 함
from . import views  # 같은 articles 내 view 를 가져옴


# /articles/ ____ , 사용자는 이미 articles 까지 들어온 상태
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),

    # path('new/', views.new, name='new'),  # views 의 new함수, new.html 생성 필요
    
    path('create/', views.create, name='create'),
    # /articles/4/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    # /articles/3/comments/
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),
    # /articles/3/comments/2/delete/
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]



