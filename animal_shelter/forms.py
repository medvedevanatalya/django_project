from django.forms import ModelChoiceField, ModelForm, DateInput
from .models import Animal, AnimalCard, ParentCard, AdoptedAnimals


class AnimalCardModelForm(ModelForm):
    animal = ModelChoiceField(label='Животное: ', queryset=Animal.objects.order_by('name'))

    class Meta:
        model = AnimalCard
        exclude = ['id', 'is_adopted']


class ParentCardModelForm(ModelForm):
    class Meta:
        model = ParentCard
        exclude = ['id']
        widgets = {
            'date_of_birth': DateInput()
        }


class AdoptedAnimalsModelForm(ModelForm):
    animal_card = ModelChoiceField(label='Животное: ', queryset=AnimalCard.objects.order_by('name'))
    parent_card = ModelChoiceField(label='Родитель: ', queryset=ParentCard.objects.order_by('fio'))

    class Meta:
        model = AdoptedAnimals
        exclude = ['id']
