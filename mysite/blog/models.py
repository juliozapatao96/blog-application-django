from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)


# Create your models here.
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, # ForeignKey: relación de uno a muchos
                               on_delete=models.CASCADE,# on_delete=models.CASCADE: si se elimina el usuario, se eliminan los posts
                               related_name='blog_posts') # related_name: nombre del campo inverso
    
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager() # default manager
    published = PublishedManager() # custom manager

    class Meta:
        ordering = ['-publish'] # el - significa que se ordena de mayor a menor
        indexes = [
            models.Index(fields=['-publish']) # crea un índice para la columna publish
        ]

    def __str__(self):
        return self.title
    