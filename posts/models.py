from django.db import models
from django.urls import reverse

# Create your models here.
import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User=get_user_model()

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        pass

    class Meta:
        ordering=['-created_at']
        unique_together=['user','message']            
