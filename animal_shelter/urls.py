import django.urls as u
from django.conf.urls import url

from . import views
from .views import ListAnimalCard


urlpatterns = [
    u.path('animals/<int:animal_id>', views.show_animal_card, name='animal-show'),
    u.path('new-animal-card', views.create_animal_card, name='new-animal-card'),
    u.path('animals/animal-card-list', ListAnimalCard.as_view()),
    u.path('animals/delete_animal_card/<int:animal_id>', views.delete_animal_card, name='delete_animal_card'),
    u.path('animals/adopted_animal/<int:animal_id>', views.adopted_animal, name='adopted_animal'),
]
