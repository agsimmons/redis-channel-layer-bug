from django.shortcuts import render


def chat_view(request):
    return render(request, "demo_app/chat.html")


def user_log_view(request):
    return render(request, "demo_app/user_log.html")
