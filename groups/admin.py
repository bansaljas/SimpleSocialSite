from django.contrib import admin
from .models import Group,GroupMembers
# Register your models here.

class GroupMembersInline(admin.TabularInline):
    model = GroupMembers

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupMembersInline]

admin.site.register(Group,GroupAdmin)
