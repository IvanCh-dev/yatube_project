from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Группа с названием {slug}')
