from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = "index.html"

def about(request):
    return render(request, "pages/contacts.html")

def materials(request):
    return render(request, 'pages/materials.html')

def lesmanager(request):
    return render(request, 'main/lesmanager.html')

def testmanager(request):
    return render(request, 'main/testmanager.html')

def video(request):
    return render(request, 'pages/video.html')
def books(request):
    return render(request, 'pages/books.html')
def lesmanager(request):
    return render(request, 'main/lesmanager.html')
def les1(request):
    return render(request, 'main/les1.html')
def les2(request):
    return render(request, 'main/les2.html')

def go_back(request):
    return HttpResponse("<script>history.back()</script>")




