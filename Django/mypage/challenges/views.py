from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "This is january!",
    "february": "This is february!",
    "march": "This is march!",
    "april": "This is april!",
    "may": "This is may!",
    "june": "This is june!",
    "july": "This is july!",
    "august": "This is August!",
    "september": "This is september!",
    "october": "This is october!",
    "november": "This is november!",
    "december": "This is december!",
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challengess.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        result = monthly_challenges[month]
        response = f"<h1>{result}</h1>"
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("<h1>Month Not Valid</h1>")

