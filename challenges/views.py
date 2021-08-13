from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# data dict
data_dict_by_month = {
    'january': 'Birthday Month',
    'february': '28 days #shortest month',
    'march': 'march'
}

# Create your views here.


def index(request):

    list_of_links = ""

    for each_month in data_dict_by_month.keys():
        path_for_each_month = reverse("month-challenge", args=[each_month])
        list_of_links += f"<li><a href=\"{path_for_each_month}\">{each_month.upper()}</a></li>"

    return HttpResponse("<ul>" + list_of_links + "</ul>")


def monthly_challenges_by_num(request, month):
    try:
        months = list(data_dict_by_month.keys())
        redirect_month = months[month-1]
        redirect_url = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_url)
    except:
        return HttpResponseNotFound("<h1>Not Found</h1>")


def monthly_challenges(request, month):
    try:
        challenge_text = data_dict_by_month[month]
        return HttpResponse(render(request, 'challenges/challenge.html', {
            "text" : challenge_text,
            "title": month
        }))
    except:
        return HttpResponseNotFound("<h2>Month Not Found</h2>")
