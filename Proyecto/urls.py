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
from TodoAnime.views import (index, OtakuList, OtakuDetail, OtakuUpdate, OtakuDelete, OtakuCreate, OtakuSearch,
                             Login, SingUp, Logout, OtakuMineList, PerfilCreate, PerfilUpDate
)
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('otaku/list', OtakuList.as_view(), name='otaku-list'),
    path('otaku/detail/<pk>', OtakuDetail.as_view(), name='otaku-detail'),
    path('otaku/update/<pk>', OtakuUpdate.as_view(), name='otaku-update'),
    path('otaku/delete/<pk>', OtakuDelete.as_view(), name='otaku-delete'),
    path('otaku/create', OtakuCreate.as_view(), name='otaku-create'),
    path('otaku/search', OtakuSearch.as_view(), name='otaku-search'),
    path('login/', Login.as_view(), name='login'),
    path('singup/', SingUp.as_view(), name='singup'),
    path('logout/', Logout.as_view(), name='logout'),
    path('otaku/mine/list', OtakuMineList.as_view(), name='mine-list'),
    path('perfil/create', PerfilCreate.as_view(), name='perfil-create'),
    path('perfil/update/<pk>', PerfilUpDate.as_view(), name='perfil-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
