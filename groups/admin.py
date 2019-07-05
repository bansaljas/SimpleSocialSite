from django.contrib import admin
from .models import Group,GroupMembers
# Register your models here.
admin.site.register(Group)

class GroupMembersInline(admin.TabularInline):
    model=GroupMembers
