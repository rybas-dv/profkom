from django.contrib import admin
from .models import *
# Register your models here.

class KonkursImageInline (admin.TabularInline):
    model = KonkursImage
    extra = 0

class KonkursAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Konkurs._meta.fields]
    inlines = [KonkursImageInline]

    class Meta:
        model = Konkurs

admin.site.register(Konkurs, KonkursAdmin)

class KonkursImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in KonkursImage._meta.fields]

    class Meta:
        model = KonkursImage

admin.site.register(KonkursImage, KonkursImageAdmin)

