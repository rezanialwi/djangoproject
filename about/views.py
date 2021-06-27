from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'subjudul':'About',
        'banner':'about/img/banner_about.png',
        'app_css':'about/css/style.css',
        
    }
    return render(request, 'about/index.html', context)

def recent(request):
    return HttpResponse("<h1>Ini adalah recent post </h1>")