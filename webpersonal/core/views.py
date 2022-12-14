from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, "core/portada.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contacto.html")
