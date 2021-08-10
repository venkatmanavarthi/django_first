from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# data dict
data_dict_by_month = {
    'january': 'Birthday Month',
    'february': '28 days #shortest month',
    'march': 'march'
}

# Create your views here.


def monthly_challenges_by_num(request, month):
    try:
        months = list(data_dict_by_month.keys())
        redirect_month = months[month-1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
    except:
        return HttpResponseNotFound("Not Found")


def monthly_challenges(request, month):
    try:
        challenge_text = data_dict_by_month[month]
    except:
        return HttpResponseNotFound("Month Not Found")
    return HttpResponse(challenge_text)
