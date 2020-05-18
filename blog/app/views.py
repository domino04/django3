from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    movie_count = Article.objects.filter(category="movie").count()
    drama_count = Article.objects.filter(category="drama").count()
    entertain_count = Article.objects.filter(category="entertain").count()  
    return render(request, 'index.html', {'movie_count' : movie_count, 'drama_count' : drama_count, 'entertain_count':entertain_count})

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('detail', pk_of_the_article_that_i_clicked=new_article.pk)
    else:
        return render(request, 'new.html')

def detail(request, pk_of_the_article_that_i_clicked):
    article = Article.objects.get(pk=pk_of_the_article_that_i_clicked)
    return render(request, 'detail.html', {'a_article' : article})

def movie(request):
    #해당 카테고리 글 제목 리스팅
    movie_article = Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'movie_article' : movie_article})
    
def drama(request):
    #해당 카테고리 글 제목 리스팅
    drama_article = Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'drama_article' : drama_article})

def entertain(request):
    #해당 카테고리 글 제목 리스팅
    entertain_article = Article.objects.filter(category="entertain")
    return render(request, 'entertain.html', {'entertain_article' : entertain_article})
