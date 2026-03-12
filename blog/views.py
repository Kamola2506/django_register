from django.shortcuts import render
from .models import Post, MeningIsmim, MeningFamilyam, University, Yoshim

def home(request):
        postlar = Post.objects.all()
        context = {'postlar': postlar}
        return render(request, 'home.html', context)

def mening_ismim(request):
    ismlar = MeningIsmim.objects.all()
    context = {
        'title': 'Mening ismim',
        'ismlar': ismlar
    }
    return render(request, 'mening_ismim.html', context)

def mening_familyam(request):
    familyalar = MeningFamilyam.objects.all()
    context = {
        'title': 'Mening familyam',
        'familyalar': familyalar
    }
    return render(request, 'mening_familyam.html', context)

def yoshim(request):
    yoshlar = Yoshim.objects.all()
    context = {
        'title': 'Mening yoshim',
        'yoshlar': yoshlar
    }
    return render(request, 'yoshim.html', context)

def university(request):
    universities = University.objects.all()
    context = {
        'title': 'Universitetim',
        'universities': universities
    }
    return render(request, 'university.html', context)

def postlar(request):
    postlar = Post.objects.all().order_by('-id')
    context = {
        'title': 'Barcha postlar',
        'postlar': postlar
    }
    return render(request, 'postlar.html', context)