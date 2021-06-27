from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'subjudul':'Blog',
        'banner':'blog/img/banner_blog.png',
        'app_css':'blog/css/style.css',
        'nav':[
            ['/', 'Home'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News'],
        ]
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul':'blog kita',
        'subjudul':'News',
    }
    return render(request, 'blog/index.html', context)
    
def cerita(request):
    context = {
        'judul':'blog kita',
        'subjudul':'Cerita',
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("<h1>Ini adalah recent post </h1>")
