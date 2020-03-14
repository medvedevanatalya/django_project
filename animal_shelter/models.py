from django.db import models
from django.db.models import fields as f
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Animal(models.Model):
    name = f.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = f.CharField(unique=True, max_length=30)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class AnimalCard(models.Model):
    name = f.CharField(max_length=20)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT)
    gender = f.CharField(max_length=7)
    age = f.CharField(max_length=15)
    state_time_admission = f.TextField()
    reason_getting_shelter = f.TextField()
    additional_inform = f.TextField()
    date_receipt = f.DateTimeField(auto_now_add=True)
    # photo = f.ImageField()
    is_adopted = f.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.name


class ParentCard(models.Model):
    fio = f.CharField(max_length=100)
    address = f.CharField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    gender = f.CharField(max_length=7)
    age = f.IntegerField()
    email = f.EmailField()

    def __str__(self):
        return self.fio


class AdoptedAnimals(models.Model):
    animal_card = models.ForeignKey(AnimalCard, on_delete=models.PROTECT)
    parent_card = models.ForeignKey(ParentCard, on_delete=models.PROTECT)
    date_adoption = f.DateTimeField(blank=True, null=True)
