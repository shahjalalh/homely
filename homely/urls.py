"""homely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # app urls
    url(r'^home/', include('home_app.urls'), name='home'),

    # django-allauth urls
    url(r'^accounts/', include('allauth.urls')),

    # Django REST framework urls
    # Browsable API you'll probably also want to add REST framework's login and logout views
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
