from django.urls import path
from . import views

app_name = 'groups'

urlpatterns=[

    path('',views.ListView.as_view(),name='all'),
    path('new/',views.CreateGroup.as_view(),name='new'),
    path('post/in/<slug>',views.SingleGroup.as_view(),name='detail')
]
