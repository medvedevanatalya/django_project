# Generated by Django 3.0.3 on 2020-03-14 17:28

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParentCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('gender', models.CharField(max_length=7)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animal_shelter.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=7)),
                ('age', models.CharField(max_length=15)),
                ('state_time_admission', models.TextField()),
                ('reason_getting_shelter', models.TextField()),
                ('additional_inform', models.TextField()),
                ('date_receipt', models.DateTimeField(auto_now_add=True)),
                ('is_adopted', models.BooleanField(blank=True, default=False)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animal_shelter.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='AdoptedAnimals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_adoption', models.DateTimeField(blank=True, null=True)),
                ('animal_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animal_shelter.AnimalCard')),
                ('parent_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animal_shelter.ParentCard')),
            ],
        ),
    ]
