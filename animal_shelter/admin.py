from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Animal)
admin.site.register(models.AnimalCard)
admin.site.register(models.ParentCard)
admin.site.register(models.AdoptedAnimals)
