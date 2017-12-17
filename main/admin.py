from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_filter = ["title",]
    search_fields = ["title", "user",]
