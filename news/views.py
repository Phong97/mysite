from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Article

# Create your views here.
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, month):
    a_list = Article.objects.filter(pub_date__month=month)
    context = {'month':month, 'article_list': a_list}
    return render(request, 'news/month_archive.html', context)

def article_detail(request, Article_id):
    article = get_object_or_404(Article, pk=Article_id)
    context = {'article':article}
    return render(request, 'news/article_detail.html', context)