from django.contrib import admin
from django.urls import path

from . import views
from django.conf.urls import handler404, handler500, handler403, handler400


handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),

]
