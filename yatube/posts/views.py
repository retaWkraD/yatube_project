#  from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)


# # В урл мы ждем парметр, и нужно его прередать в функцию для использования
# def group_posts_detail(request, pk):
#     return HttpResponse(f'Здесь Пост номер {pk}')
