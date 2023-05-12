"""djangoProject2 URL Configuration

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
from django.urls import path
from app01 import views
from app01.views import depart,user,mobile,admin,account

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('depart/list/',depart.depart_list),
    path('depart/add/',depart.depart_add),
    path('depart/delete/',depart.depart_delete),
    path('depart/<int:nid>/edit/',depart.depart_edit),
    path('user/list/',user.user_list),
    path('user/add2/',user.user_add2),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/',user.user_delete),
    path('mobile/list/',mobile.mobile_list),
    path('mobile/add/',mobile.mobile_add),
    path('mobile/<int:nid>/edit/', mobile.mobile_edit),
    path('mobile/<int:nid>/delete/', mobile.mobile_delete),
    path('admin/list/', admin.admin),
    path('admin/add/', admin.add),
    path("admin/<int:nid>/edit/",admin.edit),
    path("admin/<int:nid>/reset/",admin.reset),
    path("login/",account.login),
    path("logout/",account.Logout),
    path("image/code/", account.image_code)
]

