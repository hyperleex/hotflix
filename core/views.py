from django.shortcuts import render

# Create your views here.
from core.models import Serial, ShowCase


def home_view(request):
    serials = Serial.objects.filter(is_featured=True)
    ctx = {
        'serials': serials,
        'showcases': ShowCase.objects.all().prefetch_related('serials')
    }
    return render(request, 'core/home.html', context=ctx)


def catalog_view(request):
    return render(request, 'core/catalog.html')
