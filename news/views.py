from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {'news': news,
             'title': "Список новин",
             'categories': categories,
    }
    return render(request, template_name='news/index.html', context=context)

