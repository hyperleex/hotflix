from django.shortcuts import render

from core.models import Serial

class ShowCase:
    def __init__(self, name, serials):
        self.serials = serials
        self.name = name


def home_view(request):
    serials = Serial.objects.filter(is_featured=True)
    popular_serials = Serial.objects.exclude(is_featured=True)
    mir_sporta =  Serial.objects.filter(genres__name='Спорт')
    ctx = { 
        'serials': serials,
        'showcases': [
            ShowCase('Сейчас смотрят', popular_serials),
            ShowCase('Мир спорта', mir_sporta),
        ]
        }
    return render(request, 'core\home.html', context=ctx)

def catalog_view(request):
    serials = Serial.objects.all()
    context = {
        'serials': serials,
    }
    return render(request, 'core/catalog.html', context)