from django.shortcuts import render


def demo_view(request):
    return render(request, "demo_app/demo.html")
