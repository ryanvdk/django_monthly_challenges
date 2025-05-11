from django.urls import path
from . import views

# URL config
urlpatterns = [
    path("", views.month_list, name="challenge-list"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="monthly-challenge")
]
