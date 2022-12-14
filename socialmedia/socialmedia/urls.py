"""socialmedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/',
         admin.site.urls),
    path('',
         views.HomePage.as_view(),
         name='home'),
    path('accounts/',
         include('app_accounts.urls',
                 namespace='app_accounts')),
    path('accounts/',
         include('django.contrib.auth.urls')),
    path('test/',
          views.TestPage.as_view(),
          name='test'),
    path('thanks',
          views.ThanksPage.as_view(),
          name='thanks'),
    path('posts/',
         include(('app_posts.urls','app_posts'),
                 namespace='app_posts')),
    path('groups/',
         include(('app_groups.urls','app_groups'),
                 namespace='app_groups')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = urlpatterns + [path('__debug__/', include(debug_toolbar.urls))]
