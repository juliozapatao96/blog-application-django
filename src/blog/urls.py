from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    #El segundo patrón se asigna a la vista post_detail y solo acepta un argumento, id, que coincide con un entero, definido por el convertidor de rutas int.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', 
         views.post_detail, 
         name='post_detail'), 
    
]
