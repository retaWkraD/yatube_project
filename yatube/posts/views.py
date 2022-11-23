#  from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post


# # Create your views here.
# def index(request):
#     template = 'posts/index.html'
#     title = 'Это главная страница проекта Yatube'
#     context = {
#         'text': title,
#     }
#     return render(request, template, context)

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': title,
    }
    return render(request, template, context)


# # В урл мы ждем парметр, и нужно его прередать в функцию для использования
# def group_posts_detail(request, pk):
#     return HttpResponse(f'Здесь Пост номер {pk}')
