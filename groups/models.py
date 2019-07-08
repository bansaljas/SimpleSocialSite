from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
import misaka

from django import template
register = template.Library()

from django.contrib.auth import get_user_model
User=get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=150,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMembers")

    def __str__(self):
        self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        self.description_html=misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:detail',kwargs={'slug':self.slug})

    class Meta:
        ordering=['name']


class GroupMembers(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='memberships')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together=('group','user')
