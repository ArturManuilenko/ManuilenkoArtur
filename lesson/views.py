from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.

def all_materials(request):
    materials = models.Material.objects.all()  #если не заданы свои исп.objects получ все обьекты данного class
    return render(request,
                  'materials/all_materials.html',
                  {"materials": materials})   #контекст те переменные которые понадобятся в шаблонах

def material_details(request ,year ,month ,day, slug):
    material = get_object_or_404(models.Material,
                                 slug=slug,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(request,
                  'materials/detail.html',
                  {'material': material})