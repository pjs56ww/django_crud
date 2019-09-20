from django.urls import path, include  # 반드시 추가해줘야 함
from . import views  # 같은 jobs 내 view 를 가져옴


# /jobs/ ____ , 사용자는 이미 jobs 까지 들어온 상태
app_name = 'jobs'
urlpatterns = [
    path('', views.insert, name='insert'),
    path('past_job/', views.past_job, name='past_job'),
    path('delete/', views.delete, name='delete')
]
