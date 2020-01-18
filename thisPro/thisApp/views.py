from django.shortcuts import render

def home (request):
    return render(request, "thisApp/home.html")
