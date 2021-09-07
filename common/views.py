from django.shortcuts import render

from .data import get_features


def home(request):
    return render(request, "common/home.html")


def about(request):
    return render(request, "common/about.html", context={"features": get_features()})
