from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="home"),
    path("demand", views.demand, name="demand"),
    path("geografi", views.geografi, name="geografi"),
    path("skills", views.skills, name="skills"),
    path("vacancies", views.vacancies, name="vacancies"),
]
