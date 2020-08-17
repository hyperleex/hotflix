from django.shortcuts import render
from core.models import Serial, ShowCases


def home_view(request):
    serials = Serial.objects.filter(is_featured=True)

    context = {
        'serials': serials,
        'showcases': ShowCases.objects.all().prefetch_related('serial')
    }

    return render(request, 'core/home.html', context)


def catalog_view(request):
    serials = Serial.objects.all()
    context = {
        'serials': serials,
    }

    return render(request, 'core/catalog.html', context)
