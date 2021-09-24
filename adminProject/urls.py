"""adminProject URL Configuration

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
from django.urls import path

from adminapp.apis.views_home_page import *

from adminapp.apis.views_login_page import *

from adminapp.apis.views_create_user import *

from adminapp.apis.views_image_details import *

from adminapp.apis.views_file_details import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home_page,name='home'),

    path('login/',login_function,name='login'),

    path('logout/',logout_function,name='logout'),

    path('create_user/',CreateUserAPI.as_view(),name='create_user'),

    path('dashboard/',userDashboard,name='dashboard'),

    path('upload_image/',UploadImageAPI.as_view(),name='upload_image'),

    path('upload_file/',UploadFileAPI.as_view(),name='upload_file')


]
