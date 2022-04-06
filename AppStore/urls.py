"""AppStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('database', app.views.database, name='database'),
    path('database_provider', app.views.database_provider, name='database_provider'),
    path('add', app.views.add, name='add'),
    path('add_provider', app.views.add_provider, name='add_provider'),
    path('view/<str:id>', app.views.view, name='view'),
    path('edit/<str:id>', app.views.edit, name='edit'),
    path('<str:id>/edit', app.views.edit, name='edit'),
    path('view_provider/<str:id>', app.views.view_provider, name='view_provider'),
    path('edit_provider/<str:id>', app.views.edit_provider, name='edit_provider'),    
    path('', app.views.home, name='home'),
    path('login/', app.views.login, name='login'),
    path('login_provider/', app.views.login_provider, name='login_provider'),
    path('<str:id>/services', app.views.services, name='services'),
    path('<str:id>/job_cat/<str:service>/', app.views.job_cat, name='job_cat'),
    path('<str:id>/job_cat/<str:service>/job_req/<str:expertise>/', app.views.job_req, name='job_req'),
    path('test/', app.views.test, name='test'),
    #Testing for transaction
    path('<str:id>/job_cat/<str:service>/job_req/<str:expertise>/transaction/<str:prov_id>/', app.views.transaction, name='transaction')
]
