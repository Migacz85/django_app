from django.shortcuts import render, HttpResponse


def template(request):
    return render(request, "base.html")
