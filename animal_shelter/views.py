from django.contrib import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView

from .models import Animal, AnimalCard, ParentCard
from .forms import AnimalCardModelForm, ParentCardModelForm, AdoptedAnimalsModelForm


# Create your views here.
def show_animal_card(request, animal_id: int):
    animal_card = AnimalCard.objects.get(pk=animal_id)
    if request.GET.get('deleted'):
        delete_animal_card(request, animal_id)
    elif request.GET.get('adopted'):
        adopted_animal(request, animal_id)
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
    animal_card = AnimalCard.object.get(pk=animal_id)
    animal_card.delete()
    return render(request, 'animals/animal_card_list.html')


def update_animal_card(request, animal_id: int):
    pass
    # animal_card = AnimalCard.objects.get(pk=animal_id)
    # if request.method == "POST":
    #     animal_card.name = request.POST.get("name")
    #     animal_card.animal = request.POST.get("animal")
    #     animal_card.breed = request.POST.get("breed")
    #     animal_card.gender = request.POST.get("gender")
    #     animal_card.age = request.POST.get("age")
    #     animal_card.state_time_admission = request.POST.get("state_time_admission")
    #     animal_card.reason_getting_shelter = request.POST.get("reason_getting_shelter")
    #     animal_card.additional_inform = request.POST.get("additional_inform")
    #     animal_card.save()
    #     return redirect(show_animal_card, animal_card.id)
    # else:
    #     return render((request, ''))


def adopted_animal(request, animal_id: int):
    animal_card = AnimalCard.object.get(pk=animal_id)
    animal_card.is_adopted = True
    return redirect(show_animal_card, animal_card.id)


class ListAnimalCard(ListView):
    model = AnimalCard
    queryset = AnimalCard.objects.all()
    template_name = 'animals/animal_card_list.html'
