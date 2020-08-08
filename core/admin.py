from django.contrib import admin

# Register your models here.
from core.models import Serial, Genre, Series


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'is_buy_forever')


admin.site.register(Genre)
admin.site.register(Series)
