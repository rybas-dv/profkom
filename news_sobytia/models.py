from django.contrib.auth.models import User
from django.db import models

class SmotrKonkurs(models.Model):
    name = models.CharField(max_length=128, blank=True, default=None)
    text = models.TextField(blank=True, default=None)
    comments = models.TextField(blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "смотр-конрус %s" % self.id
    class Meta:
        verbose_name = "смотр-конкурс"
        verbose_name_plural = "смотры-конкурсы"

class SmotrKonkursImage(models.Model):
    konkurs = models.ForeignKey(SmotrKonkurs, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='static/img/', blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.id
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"