from django.urls import path, re_path
from . import views

app_name = 'app_posts'

urlpatterns = [
    path('',
         views.PostList.as_view(),
         name = 'all'),
    path('new',
         views.CreatePost.as_view(),
         name = 'create'),
    re_path('by/(?P<username>[-\w]+)',
         views.UserPost.as_view(),
         name='for_user'),
    re_path('by/(?P<pk>[-\w]+)',
         views.PostDetail.as_view(),
         name='single'),
    re_path('delete/(?P<pk>\d+)',
         views.DeletePost.as_view(),
         name='delete'),
         ]
