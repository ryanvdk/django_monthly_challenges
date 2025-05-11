from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def handle_month(month):
    try:
        return challenges[month]
    except:
        return HttpResponseNotFound("404 month not found")


def monthly_challenge(request, month):
    return HttpResponse(handle_month(month))
