from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import (ListView,DetailView,
                                  CreateView,RedirectView)
from .models import Group,GroupMembers
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

class CreateGroup(LoginRequiredMixin,CreateView):
    model=Group
    fields=('name','description')

class SingleGroup(LoginRequiredMixin,DetailView):
    model=Group

class ListGroups(LoginRequiredMixin,ListView):
    model=Group

class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse ('groups:detail',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMembers.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,"Warning! You are already a member of {}".format(group.name))

        else:
            messages.success(self.request,"Welcome! You are now a member of {}".format(group.name))

        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse ('groups:detail',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = GroupMembers.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()

        except GroupMembers.DoesNotExist:
            messages.warning(self.request,"You can't leave this group because you aren't in it.")

        else:
            membership.delete()
            messages.success(self.request,"You have successfully left this group.")

        return super().get(request,*args,**kwargs)
