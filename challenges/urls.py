from django.urls import path
from . import views


urlpatterns = [
    # dynamic path using angular brackets <>
    path("", views.index),
    path("<int:month>", views.monthly_challenges_by_num),
    path("<str:month>", views.monthly_challenges, name='month-challenge')
]
