from django.contrib import admin

# Register your models here.
from core.models import Serial, Genre, Series, ShowCases

@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_featured', 'is_buy_forever')


admin.site.register(Genre)
admin.site.register(Series)
admin.site.register(ShowCases)
