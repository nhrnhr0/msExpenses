"""Project URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers

from core.views import ApprovedOrdersViewSet, GeneralOrdersViewSet, index_view,approve_general_order

svelteRouter = routers.DefaultRouter()
svelteRouter.register(r'general', GeneralOrdersViewSet)
svelteRouter.register(r'approved', ApprovedOrdersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(svelteRouter.urls)),
    path('', index_view, name='index'),
    re_path('approve-go/(?P<item_id>\d+)/$', approve_general_order, name='approve_general_order')
]
