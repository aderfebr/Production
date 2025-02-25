"""
URL configuration for Production project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path
from app import views

urlpatterns = [
    path('rule', TemplateView.as_view(template_name='index.html')),
    path('judge', TemplateView.as_view(template_name='index.html')),
    path("api/getnode/", views.getnode),
    path("api/addnode/", views.addnode),
    path("api/deletenode/", views.deletenode),
    path("api/getedge/", views.getedge),
    path("api/addedge/", views.addedge),
    path("api/deleteedge/", views.deleteedge),
    path("api/forward/",views.forward),
    path("api/backward/",views.backward),
]
