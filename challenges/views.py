from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
challenges = {
    "january": "Read a book",
    "february": "Go for a walk",
    "march": "Eat cheese",
    "april": "Jump up and down",
    "may": "have a party",
    "june": "make money",
    "july": "run far",
    "august": "swim far",
    "september": "Take a test",
    "october": "Buy a bicycle",
    "november": "win a game",
    "december": "make a friend"
}


def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "monthly-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("404 month not found")


def month_list(request):
    month_list = ""
    for month in list(challenges.keys()):
        month_path = reverse("monthly-challenge", args=[month])
        month_list += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    response_data = f"<h1>List</h1><ul>{month_list}</ul>"
    return HttpResponse(response_data)
