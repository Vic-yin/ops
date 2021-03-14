"""api URL Configuration

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
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('vic/shop/api/v1/',views.api_1),
    path('vic/shop/api/v2/', views.api_2),
    path('vic/shop/api/v3/', views.api_3),
    path('vic/shop/api/v4/', views.api_4),
    path('vic/shop/api/v5/', views.api_5),
    path('vic/shop/api/v6/', views.api_6),
    path('vic/shop/api/v7/', views.api_7),
    path('vic/shop/api/v8/', views.api_8),
    path('vic/shop/api/v9/', views.api_9),
    path('vic/shop/api/v10/', views.api_10),
    path('vic/shop/api/v11/', views.api_11),
    path('vic/shop/api/v12/', views.api_12),
    path('vic/shop/api/v13/', views.api_13),
    path('vic/shop/api/v14/', views.api_14),
]
