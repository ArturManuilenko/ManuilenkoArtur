from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from . import models
from . import forms


# Create your views here.

def all_materials(request):
    materials = models.Material.objects.all()  # если не заданы свои исп.objects получ все обьекты данного class
    return render(request,
                  'materials/all_materials.html',
                  {"materials": materials})  # контекст те переменные которые понадобятся в шаблонах


def material_details(request, year, month, day, slug):
    material = get_object_or_404(models.Material,
                                 slug=slug,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    return render(request,
                  'materials/detail.html',
                  {'material': material})


def share_material(request, material_id):
    material = get_object_or_404(models.Material,
                                 id=material_id)

    if request.method == 'POST':
        form = forms.EmailMaterialForm(request.POST)
        if form.is_valid():  # делаем проверку на все поля/ значения попадают в cd
            cd = form.cleaned_data  # инфа переданая пользователем после валидации ввиде словаря
            material_uri = request.build_absolute_uri(
                material.get_absolute_url()
            )

            subject = "{} asks you to review next material: {}".format(
                cd['name'],
                material.title,
            )

            body = ("{title} at {uri} \n\n {name} asks you to review it."
                    "Comment:\n\n {comment}").format(
                title=material.title,
                uri=material_uri,
                name=cd['name'],
                comment=cd['comment'],
            )

            send_mail(subject,
                      body,
                      'supersiteadmin@mysite.com',
                      [cd['to_email'], ])
    else:
        form = forms.EmailMaterialForm()

    return render(request,
                  'materials/share.html',
                  {'material': material, 'form': form})
