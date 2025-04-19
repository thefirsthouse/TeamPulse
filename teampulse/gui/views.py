from django.shortcuts import render


def index(request):
    user = request.user
    return render(request, "gui/index.html", {"user": user})
