from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")
def demand(request):
    return render(request, "main/demand.html")
def geografi(request):
    return render(request, "main/geografi.html")
def skills(request):
    return render(request, "main/skills.html")
def vacancies(request):
    return render(request, "main/vacancies.html")
# Create your views here.
