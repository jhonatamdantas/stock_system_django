from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("cadastrar_produto/", views.register_product, name='register'),
    path("editar/", views.edit, name='edit'),
    path("atualizar/<int:pk>/", views.update, name='update'),
    path("deletar/<int:pk>/", views.delete, name='delete'),
]