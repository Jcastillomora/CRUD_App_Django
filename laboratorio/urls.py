from django.urls import path
from .views import insertar_lab_view, mostrar_lab_view, editar_lab_view, eliminar_lab_view 

urlpatterns = [
    path('', mostrar_lab_view, name='mostrar_lab_view'),
    path('mostrar/', mostrar_lab_view, name='mostrar_lab_view'),
    path('insertar/', insertar_lab_view, name='insertar_lab_view'),
    path('editar/<int:pk>/', editar_lab_view, name='editar_lab_view'),
    path('eliminar/<int:pk>/', eliminar_lab_view, name='eliminar_lab_view'),
]
