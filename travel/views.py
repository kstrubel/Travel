from django.shortcuts import render

from django.http import HttpResponse


def index(request):

    content = {}
    return render(request, 'travel/index.html', content)


def about(request):

    content = {}
    return render(request, 'travel/about.html', content)


def country(request, country_code):
    webpage = 'travel/country/' + country_code + '.html'
    content = {
        'country_code': country_code,
    }
    return render(request, webpage, content)

