from django.http import HttpResponse
from django.shortcuts import render

#method view index
def index(request):
    context = {
        'judul':'kelas terbuka',
        'subjudul':'home',
        'banner':'img/banner_home.png',
        'nav':[
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact'],
        ]
    }
    return render(request, 'index.html', context)

# def about(request):
#     return render(request, 'about.html')
# def index2(request):

#     judul = "<h1> ini adalah Home</h1>"
#     subjudul = "<h1> Selamat datang diwebsite</h1>"
#     output = judul + subjudul
#     return HttpResponse(output)
