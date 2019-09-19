from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 추가할 때 현재시간을 기록하겠다??
    updated_at = models.DateTimeField(auto_now=True) # 언제든지 자동으로 현재시간을 기록하겠다.
    
# $python manage.py makemigrations  => django한테 model을 만든 사항을 알려줌 0001_initial 이 만들어짐
# $python manage.py migrate  => migrations 적용
# 다음 step crud/urls.py setting