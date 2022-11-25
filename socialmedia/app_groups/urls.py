from django.urls import path, re_path
from . import views

app_name = 'app_groups'

urlpatterns = [
    path('',
         views.ListGroup.as_view(),
         name = 'all'),
    path('new',
         views.CreateGroup.as_view(),
         name = 'create'),
    re_path('posts/in/(?P<slug>[-\w]+)',
         views.SingleGroup.as_view(),
         name='single'),
         # <slug:slug>
    ]
