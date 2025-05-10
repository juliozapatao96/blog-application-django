from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404



# Create your views here.
def post_list(request):
    posts = Post.published.all() # Post.published es el manager personalizado
    return render(request, 'blog/post/list.html', {'posts': posts}) # el primer parámetro es el request, el segundo es la plantilla y el tercero es el contexto

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