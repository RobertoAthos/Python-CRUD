from django.urls import path
from .views import create,index,edit,delete

urlpatterns = [
    path('', index, name='index'),
    path('criar/',create, name='criar'),
    path('editar/<int:user_id>',edit ,name='editar'),
    path('deletar/<int:user_id>', delete , name='deletar')
]