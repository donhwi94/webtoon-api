from django.urls import path

from . import views

urlpatterns = [
    path("", views.InterestList.as_view(), name="interest-list"),
    path("<int:interest_id>/", views.InterestDetail.as_view()),
]
