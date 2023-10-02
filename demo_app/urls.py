from django.urls import path

from demo_app import views


urlpatterns = [
    path("", views.chat_view),
    path("user_log/", views.user_log_view),
]
