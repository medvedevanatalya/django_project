from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, UpdateView

from .models import AnimalCard, ParentCard, AdoptedAnimals
from .forms import AnimalCardModelForm, ParentCardModelForm, AdoptedAnimalsModelForm

from django.contrib.auth.models import User


# вьюхи по работе с животными (перенести их в отдельный файл)
def show_animal_card(request, animal_id: int):
    animal_card = AnimalCard.objects.get(pk=animal_id)
    adopted: AdoptedAnimals
    if animal_card.is_adopted is True:
        adopted = AdoptedAnimals.objects.get(animal_card_id=animal_id)
        return render(request, 'animals/show_animal_card.html', context={'animal_card': animal_card, 'adopted': adopted})
    else:
        return render(request, 'animals/show_animal_card.html', context={'animal_card': animal_card})


def create_animal_card(request):
    if request.method == 'GET':
        return render(request, 'animals/form_animal_card.html', context=dict(form=AnimalCardModelForm()))
    elif request.method == 'POST':
        form = AnimalCardModelForm(request.POST)
        if form.is_valid():
            animal_card = form.save()
            return redirect(show_animal_card, animal_card.id)
        else:
            return render(request, 'animals/form_animal_card.html', context=dict(form=form))


def delete_animal_card(request, animal_id: int):
    animal_card = AnimalCard.objects.get(pk=animal_id)
    animal_card.delete()  # при удалении ошибка, так как нельзя удалить животное, которое усыновлено
    return redirect('/animal/animals/list_animal_card')


class ListAnimalCard(ListView):
    model = AnimalCard
    queryset = AnimalCard.objects.all()
    template_name = 'animals/list_animal_card.html'


class AnimalCardUpdate(UpdateView):
    model = AnimalCard
    form_class = AnimalCardModelForm
    template_name = 'animals/update_animal_card.html'

    def get_success_url(self):
        return reverse('list-animal-card')


# вьюхи по работе с родителями (перенести их в отдельный файл)
def show_parent_card(request, parent_id: int):
    parent_card = ParentCard.objects.get(pk=parent_id)
    return render(request, 'parents/show_parent_card.html', context={'parent_card': parent_card})


def create_parent_card(request):
    if request.method == 'GET':
        return render(request, 'parents/form_parent_card.html', context=dict(form=ParentCardModelForm()))
    elif request.method == 'POST':
        form = ParentCardModelForm(request.POST)
        if form.is_valid():
            parent_card = form.save()
            return redirect(show_parent_card, parent_card.id)
        else:
            return render(request, 'parents/form_parent_card.html', context=dict(form=form))


def delete_parent_card(request, parent_id: int):
    parent_card = ParentCard.objects.get(pk=parent_id)
    parent_card.delete()  # при удалении ошибка, так как нельзя удалить родителя, который усыновил животное
    return redirect('/animal/parents/list_parent_card')


class ListParentCard(ListView):
    model = ParentCard
    queryset = ParentCard.objects.all()
    template_name = 'parents/list_parent_card.html'


class ParentCardUpdate(UpdateView):
    model = ParentCard
    form_class = ParentCardModelForm
    template_name = 'parents/update_parent_card.html'

    def get_success_url(self):
        return reverse('list-parent-card')


# вьюхи по работе с усыновлением животного (перенести их в отдельный файл)
def show_adopted(request, adopted_id: int):
    adopted = AdoptedAnimals.objects.get(pk=adopted_id)
    return render(request, 'adopted/show_adopted.html', context={'adopted': adopted})


def create_adopted(request):
    if request.method == 'GET':
        return render(request, 'adopted/form_adopted.html', context=dict(form=AdoptedAnimalsModelForm()))
    elif request.method == 'POST':
        form = AdoptedAnimalsModelForm(request.POST)
        if form.is_valid():
            adopted = form.save()
            animal_card = AnimalCard.objects.get(pk=adopted.animal_card_id)
            animal_card.is_adopted = True
            animal_card.save()
            return redirect(show_adopted, adopted.id)
        else:
            return render(request, 'adopted/form_adopted.html', context=dict(form=form))


def delete_adopted(request, adopted_id: int):
    adopted = AdoptedAnimals.objects.get(pk=adopted_id)
    adopted.delete()
    return redirect('/animal/adopted/list_adopted')


class ListAdopted(ListView):
    model = AdoptedAnimals
    queryset = AdoptedAnimals.objects.all()
    template_name = 'adopted/list_adopted.html'


class AdoptedUpdate(UpdateView):
    model = AdoptedAnimals
    form_class = AdoptedAnimalsModelForm
    template_name = 'adopted/update_adopted.html'

    def get_success_url(self):
        return reverse('list-adopted')
