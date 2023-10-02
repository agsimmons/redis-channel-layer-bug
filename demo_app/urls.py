from django.urls import path

from demo_app import views


urlpatterns = [
    path("", views.demo_view),
]
