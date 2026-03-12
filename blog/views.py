from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'home.html')


def mening_ismim(request):
    return render(request, 'mening_ismim.html')

def mening_familyam(request):
    return render(request, 'mening_familyam.html')


def yoshim(request):
    return render(request, 'yoshim.html')

def university(request):
    return render(request, 'university.html')

def postlar(request):
    postlar = Post.objects.all()
    context = {
        'postlar': postlar}
    return render(request, 'postlar.html', context)
