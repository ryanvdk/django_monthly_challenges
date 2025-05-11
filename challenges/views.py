from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": None
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
        return render(request, "challenges/challenge.html", {
            "month": month,
            "challenge_text": challenge_text
        })
    except:
        return HttpResponseNotFound("404 month not found")


def month_list(request):
    try:
        months = list(challenges.keys())
        return render(request, "challenges/index.html", {
            "months": months
        })
    except:
        return HttpResponseNotFound("404 page not found")
