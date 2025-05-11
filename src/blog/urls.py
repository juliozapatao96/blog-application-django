from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    # post views
    #path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'), # Cambiado a la vista basada en clase PostListView
    #El segundo patrón se asigna a la vista post_detail y solo acepta un argumento, id, que coincide con un entero, definido por el convertidor de rutas int.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', 
         views.post_detail, 
         name='post_detail'),
    path('<int:post_id>/share/',
         views.post_share, name='post_share'), 
    
]
