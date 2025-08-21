from django.shortcuts import render
from .models import Snews

def snewss(request):
    sns = Snews.objects.all()
    return render(request, 'snews/snewss.html', {'sns': sns})
