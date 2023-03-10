"""taskmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from todolist_app import views as todolist_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/',include('todolist_app.urls')),
    path('accounts/',include('users_app.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',todolist_views.index,name="index"),
    path('about/',todolist_views.about,name='about'),
    path('APART/',todolist_views.APART,name='APART'),
    path('contact/',todolist_views.contact,name='contact'),
    path('results/',todolist_views.test1,name='test1'),
    path('contact/request/',todolist_views.get_request_contact,name='get_request_contact'),
    path('request_call/',todolist_views.request_call_details,name='request_call_details'),
    path('careers/',todolist_views.careers,name='careers'),
    
] 
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
