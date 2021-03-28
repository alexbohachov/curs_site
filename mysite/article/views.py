from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Article
from .forms import ArticleForm


def index(request):
    article = Article.objects.all()
    return render(request, "index.html", {'articles': article})


def create(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            created = form.save()
        return redirect('detail', created.id)
    return render(request, 'article_templates/create.html', {'form': form})


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article_templates/detail.html', {'article': article})