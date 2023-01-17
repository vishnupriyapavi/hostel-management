from django.contrib import admin

from mainapp import models

# Register your models here.
admin.site.register(models.Login)
admin.site.register(models.student)
admin.site.register(models.parent)
