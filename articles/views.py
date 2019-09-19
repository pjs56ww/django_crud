from django.shortcuts import render, redirect
from .models import Article

# templates 폴더 생성 => templates가 중복되지 않도록 templates 내에 articles 폴더 추가로 생성

# articles 의 메인 페이지, article list 를 보여줌
def index(request):
    # article 내에 모든 data를 받아오겠다.
    # SELECT * FROM 과 동일한 문구(SQLite3))
    articles = Article.objects.all()  
    context = {'articles': articles}
    # 순서 중요, 세번째는 무엇을 넘겨줄지가 들어갸아한다. 
    return render(request, 'articles/index.html', context)


# Variable Routing 으로 사용자가 보기를 원하는 페이지 pk 를 받아서
# Detail 페이지를 보여준다.
def detail(request, article_pk):
    # SELECtT * FROM article WHERE pk=
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)


# 입력 페이지 제공
def new(request):
    return render(request, 'articles/new.html')


# 데이터를 전달 받아서 article 생성
def create(request):

    # new 가 전달한 data들을 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 인스턴스 생성
    article = Article()
    article.title = title
    article.content = content
    article.save()

    # <a href="/articles/">와 같은 역할 => redirect import해줘야함


    return redirect(f'/articles/{article.pk}/')


# 사용자로부터 받은 article_pk 값에 해당하는 데이터 삭제
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()

    return redirect('/articles/')