"""crud URL Configuration

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
from django.urls import path, include  # include 반드시 선언 필요

from django.conf import settings
from django.conf.urls.static import static

# 사용자가 가장 먼저 들어오는 entry point
urlpatterns = [
    
    # 다음 step => articles 에 urls.py 생성
    # /jobs/ 로 들어왔다면 jobs/urls.py 로 이동하도록 설정
    path('jobs/', include('jobs.urls')),

    # /articles/ 로 들어왔다면 articles/urls.py 로 이동하도록 설정
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]


# 사용자가 Media 파일이 있는 곳으로 올 수 있는 경로를 추가한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)