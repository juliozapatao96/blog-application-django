from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'), 
    #El segundo patrón se asigna a la vista post_detail y solo acepta un argumento, id, que coincide con un entero, definido por el convertidor de rutas int.
]
