from django.db import models
from django.db.models import fields as f
from phonenumber_field.modelfields import PhoneNumberField


GENDER_CHOICES = (
    ('мужской', "мужской"),
    ('женский', "женский"),
)
ANIMAL_CONDITION_CHOICES = (
    ('отличное', 'отличное'),
    ('хорошее', 'хорошее'),
    ('удовлетворительное', 'удовлетворительное'),
    ('плохое', 'плохое'),
)


# Create your models here.
class Animal(models.Model):
    name = f.CharField(unique=True, max_length=20, verbose_name='Животное: ')

    def __str__(self):
        return self.name


class AnimalCard(models.Model):
    name = f.CharField(max_length=20, verbose_name='Имя: ')
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, verbose_name='Животное: ')
    breed = f.CharField(max_length=15, blank=True, verbose_name='Порода: ')
    gender = f.CharField(max_length=7, choices=GENDER_CHOICES, verbose_name='Пол: ')
    age = f.CharField(max_length=15, blank=True, verbose_name='Возраст: ')
    state_time_admission = f.CharField(max_length=18, choices=ANIMAL_CONDITION_CHOICES,
                                       verbose_name='Состояние на момент приема: ')
    reason_getting_shelter = f.TextField(verbose_name='Причина приема: ')
    additional_inform = f.TextField(blank=True, verbose_name='Дополнительная информация: ')
    date_receipt = f.DateTimeField(auto_now_add=True, verbose_name='Дата приема: ')
    # photo = f.ImageField()
    is_adopted = f.BooleanField(blank=True, default=False, verbose_name='Усыновлен? ')

    def __str__(self):
        return self.name


class ParentCard(models.Model):
    fio = f.CharField(max_length=100, verbose_name='ФИО: ')
    address = f.CharField(max_length=100, verbose_name='Адрес: ')
    phone_number = PhoneNumberField(null=False, unique=True, verbose_name='Номер телефона: ')
    gender = f.CharField(max_length=7, choices=GENDER_CHOICES, verbose_name='Пол: ')
    date_of_birth = f.DateTimeField(verbose_name='Дата рождения: ', blank=True, null=True)
    email = f.EmailField(verbose_name='E-mail: ')

    def __str__(self):
        return self.fio


class AdoptedAnimals(models.Model):
    animal_card = models.ForeignKey(AnimalCard, on_delete=models.PROTECT, verbose_name='Карта животного: ')
    parent_card = models.ForeignKey(ParentCard, on_delete=models.PROTECT, verbose_name='Карта родителя: ')
    date_adoption = f.DateTimeField(auto_now_add=True, verbose_name='Дата усыновления: ')

    def __str__(self):
        return self.animal_card, self.parent_card
