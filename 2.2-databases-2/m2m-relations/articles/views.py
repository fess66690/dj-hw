from django.shortcuts import render
from .models import Article


def articles_list(request):
    template = 'articles/news.html'

    # Получаем статьи с оптимизацией запросов
    # prefetch_related для загрузки всех scopes и tags одним запросом
    articles = Article.objects.all().prefetch_related('scopes__tag').order_by('-published_at')

    context = {
        'object_list': articles,
    }

    return render(request, template, context)