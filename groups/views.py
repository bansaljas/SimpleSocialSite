from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import (ListView,DetailView,
                                  CreateView,)
from .models import Group,GroupMembers
# Create your views here.

class CreateGroup(LoginRequiredMixin,CreateView):
    model=Group
    fields=('name','description')

class SingleGroup(LoginRequiredMixin,DetailView):
    model=Group

class ListGroups(LoginRequiredMixin,ListView):
    model=Group        
