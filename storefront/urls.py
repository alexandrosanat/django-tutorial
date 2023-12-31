"""
URL configuration for storefront project.

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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from articles import views as article_views

import articles.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"^articles/", include(articles.urls)),
    path("__debug__/", include(debug_toolbar.urls)),
    # We don't put the trailing $ here as this is not the end of the url
    re_path(r"^accounts/", include("accounts.urls")),
    path("", article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
