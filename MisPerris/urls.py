"""MisPerris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from Pagina import views as viewsPag
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.auth_login, name='login'),
    url(r'^logout/$', auth_views.auth_logout, name='logout'),
	url(r'^$', viewsPag.pagina_principal,  name='pagina_principal'),
	url(r'^', include('Pagina.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^salir/$', viewsPag.logOut, name='logOut'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)