import django.urls as u
from django.conf.urls import url

from . import views
from .views import ListAnimalCard, AnimalCardUpdate, ListParentCard, ParentCardUpdate, ListAdopted, AdoptedUpdate

urlpatterns = [
    u.path('animals/<int:animal_id>', views.show_animal_card, name='show-animal'),  # показать карту животного
    u.path('new_animal_card', views.create_animal_card, name='new-animal-card'),    # создать карту животного
    u.path('animals/list_animal_card', ListAnimalCard.as_view(), name='list-animal-card'), # показать список карт животных
    u.path('animals/delete_animal_card/<int:animal_id>', views.delete_animal_card, name='delete_animal_card'),  # удалить карту животного
    u.path('animals/update_animal_card/<int:pk>', AnimalCardUpdate.as_view(), name='update_animal_card'),  # изменить карту животного
    # u.path('animals/adopted_animal/<int:animal_id>', views.adopted_animal, name='adopted_animal'),  # усыновить животного

    u.path('parents/<int:parent_id>', views.show_parent_card, name='show-parent'),  # показать карту родителя
    u.path('new_parent_card', views.create_parent_card, name='new-parent-card'),  # создать карту родителя
    u.path('parents/list_parent_card', ListParentCard.as_view(), name='list-parent-card'),  # показать список карт родителей
    u.path('parents/delete_parent_card/<int:parent_id>', views.delete_parent_card, name='delete_parent_card'),  # удалить карту родителя
    u.path('parents/update_parent_card/<int:pk>', ParentCardUpdate.as_view(), name='update_parent_card'),  # изменить карту родителя

    u.path('adopted/<int:adopted_id>', views.show_adopted, name='show-adopted'),  # показать информацию об усыновлении
    u.path('new_adopted', views.create_adopted, name='new-adopted'),  # усыновить животное
    u.path('adopted/list_adopted', ListAdopted.as_view(), name='list-adopted'),  # показать список усыновленных
    u.path('adopted/delete_adopted/<int:adopted_id>', views.delete_adopted, name='delete_adopted'),  # удалить информацию об усыновлении
    u.path('adopted/update_adopted/<int:pk>', AdoptedUpdate.as_view(), name='update_adopted'),  # изменить информацию об усыновлении
]
