"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from login.views import a, b, c, register,e,logout_view,sd,td,hd
from django.conf.urls.static import static
from django.conf import settings
from hoddata.views import save
from techdata.views import saves
from stddata.views import saveas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a, name="mainpage"),
    path('gallary2/', e, name="hello"),
    path('gallary/', b, name="checking"),
    path('logout/',logout_view,name="lg"),
    path('reg/', c, name="regpage"),
    path('fun/', register, name="page"),
    path('std/', sd, name="student"),
    path('tec/', td, name="techer"),
    path('hod/', hd, name="head"),
    path('save/', save, name="save"),
    path('saves/', saves, name="saves"),
    path('saveas/', saveas, name="saveas"),

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)