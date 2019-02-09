"""soundLicence URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework import routers


from users.views import UserViewSet
from users.views import GroupViewSet

from violation.views import LicenseeViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-types',GroupViewSet)
router.register(r'licensee', LicenseeViewSet)


api_urls = [
    url(r'^', include(router.urls)),
    path('', include('users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
    path('', TemplateView.as_view(template_name='index.html')),
]
