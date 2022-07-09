from django.db import models
from django.contrib.auth.models import User
from django_prometheus.models import ExportModelOperationsMixin
from django.urls import reverse
# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status=1)
    
    
class Post(ExportModelOperationsMixin('post'), models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title
    
    objects =  models.Manager()
    published = PublishedManager()
    
    def get_absoulute_url(self):
        return reverse('blog:post_detail', args=[self.slug])