from django.contrib import admin
from .models import *
# Register your models here.

class KonkursImageInline (admin.TabularInline):
    model = SmotrKonkursImage
    extra = 0

class KonkursAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SmotrKonkurs._meta.fields]
    inlines = [KonkursImageInline]

    class Meta:
        model = SmotrKonkurs

admin.site.register(SmotrKonkurs, KonkursAdmin)

class KonkursImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in SmotrKonkursImage._meta.fields]

    class Meta:
        model = SmotrKonkursImage

admin.site.register(SmotrKonkursImage, KonkursImageAdmin)

