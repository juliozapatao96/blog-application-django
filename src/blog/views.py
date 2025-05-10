from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView

'''
# Create your views here.
def post_list(request):
    post_list = Post.published.all() # Post.published es el manager personalizado
    # Paginator with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # si la página no es un número entero, devuelve la primera página
        posts = paginator.page(1)
    except EmptyPage:
        # si la página no existe, devuelve la última página    
        posts = paginator.page(paginator.num_pages) 
    return render(request, 
                  'blog/post/list.html', 
                  {'posts': posts}) # el primer parámetro es el request, el segundo es la plantilla y el tercero es el contexto
'''
def post_detail(request, year, month, day, post):
    # get_object_or_404: obtiene el objeto o devuelve un error 404 si no existe
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
        'blog/post/detail.html',
        {'post': post})

class PostListView(ListView):
    """Alternative class-based view for listing posts."""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'