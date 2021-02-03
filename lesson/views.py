from django.shortcuts import render
from . import models


# Create your views here.

def all_materials(request):
    materials = models.Material.objects.all()  #если не заданы свои исп.objects получ все обьекты данного class
    return render(request,
                  'materials/all_materials.html',
                  {"materials": materials})   #контекст те переменные которые понадобятся в шаблонах
