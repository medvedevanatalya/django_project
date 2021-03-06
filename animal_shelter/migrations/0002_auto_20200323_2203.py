# Generated by Django 3.0.3 on 2020-03-23 16:03

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('animal_shelter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parentcard',
            name='age',
        ),
        migrations.AddField(
            model_name='animalcard',
            name='breed',
            field=models.CharField(blank=True, max_length=15, verbose_name='Порода: '),
        ),
        migrations.AddField(
            model_name='parentcard',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения: '),
        ),
        migrations.AlterField(
            model_name='adoptedanimals',
            name='animal_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animal_shelter.AnimalCard', verbose_name='Карта животного: '),
        ),
        migrations.AlterField(
            model_name='adoptedanimals',
            name='date_adoption',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата усыновления: '),
        ),
        migrations.AlterField(
            model_name='adoptedanimals',
            name='parent_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animal_shelter.ParentCard', verbose_name='Карта родителя: '),
        ),
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Животное: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='additional_inform',
            field=models.TextField(blank=True, verbose_name='Дополнительная информация: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='age',
            field=models.CharField(blank=True, max_length=15, verbose_name='Возраст: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animal_shelter.Animal', verbose_name='Животное: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='date_receipt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата приема: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='gender',
            field=models.CharField(choices=[('мужской', 'мужской'), ('женский', 'женский')], max_length=7, verbose_name='Пол: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='is_adopted',
            field=models.BooleanField(blank=True, default=False, verbose_name='Усыновлен? '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Имя: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='reason_getting_shelter',
            field=models.TextField(verbose_name='Причина приема: '),
        ),
        migrations.AlterField(
            model_name='animalcard',
            name='state_time_admission',
            field=models.CharField(choices=[('отличное', 'отличное'), ('хорошее', 'хорошее'), ('удовлетворительное', 'удовлетворительное'), ('плохое', 'плохое')], max_length=18, verbose_name='Состояние на момент приема: '),
        ),
        migrations.AlterField(
            model_name='parentcard',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Адрес: '),
        ),
        migrations.AlterField(
            model_name='parentcard',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail: '),
        ),
        migrations.AlterField(
            model_name='parentcard',
            name='fio',
            field=models.CharField(max_length=100, verbose_name='ФИО: '),
        ),
        migrations.AlterField(
            model_name='parentcard',
            name='gender',
            field=models.CharField(choices=[('мужской', 'мужской'), ('женский', 'женский')], max_length=7, verbose_name='Пол: '),
        ),
        migrations.AlterField(
            model_name='parentcard',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона: '),
        ),
        migrations.DeleteModel(
            name='Breed',
        ),
    ]
