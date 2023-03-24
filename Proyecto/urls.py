"""Proyecto URL Configuration

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
from TodoAnime.views import index, OtakuList, OtakuDetail, OtakuUpdate, OtakuDelete, OtakuCreate, OtakuSearch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('otaku/list', OtakuList.as_view(), name='otaku-list'),
    path('otaku/detail/<pk>', OtakuDetail.as_view(), name='otaku-detail'),
    path('otaku/update/<pk>', OtakuUpdate.as_view(), name='otaku-update'),
    path('otaku/delete/<pk>', OtakuDelete.as_view(), name='otaku-delete'),
    path('otaku/create', OtakuCreate.as_view(), name='otaku-create'),
    path('otaku/search', OtakuSearch.as_view(), name='otaku-search'),
]

