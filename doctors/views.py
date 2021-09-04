from django.shortcuts import render

doc = "doctors"


def home(request):
    return render(request, f"{doc}/home.html")
