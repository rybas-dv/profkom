from django.contrib.auth.models import User
from django.db import models

# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     user = models.ForeignKey(User)
#
#     def __str__(self):
#         return self.title

# Create your models here.

class Konkurs(models.Model):
    name = models.CharField(max_length=128, blank=True, default=None)
    text = models.TextField(blank=True, default=None)
    comments = models.TextField(blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "конрус %s" % self.id
    class Meta:
        verbose_name = "конкурс"
        verbose_name_plural = "конкурсы"

class KonkursImage(models.Model):
    konkurs = models.ForeignKey(Konkurs, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='static/img/', blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.id
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"