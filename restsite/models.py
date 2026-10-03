from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="base_author")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title