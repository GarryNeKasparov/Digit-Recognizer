from django.urls import path, include
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='paint/', permanent=True)),
    path('paint/', views.index, name='index'),
]
