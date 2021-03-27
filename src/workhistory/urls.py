"""workhistory URL Configuration

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
from pages.views import home_view, contact_view, about_view, social_view
from work.views import (work_detail_view,
                        work_create_view,
                        render_initial_data,
                        dynamic_lookup_view,
                        work_delete_view,
                        work_list_view,
                        )

urlpatterns = [
    path('', home_view, name='home'),
    path('works/', work_list_view, name='work_list'),
    path('contact/', contact_view),
    path('work/', work_detail_view),
    path('create/', work_create_view),
    path('initial/', render_initial_data),
    path('work/<int:id>/', dynamic_lookup_view, name="id_work"),
    path('work/<int:id>/delete/', work_delete_view, name="work_delete"),
    path('about/', about_view),
    path('social/', social_view),
    path('admin/', admin.site.urls),
]
