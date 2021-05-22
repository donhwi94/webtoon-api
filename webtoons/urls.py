from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.WebtoonList.as_view()),
    path("<int:webtoon_id>/episodes/", views.WebtoonDetail.as_view()),
    path("<int:webtoon_id>/episodes/<int:episode_id>/", views.EpisodeDetail.as_view()),
    path(
        "<int:webtoon_id>/episodes/<int:episode_id>/comments/", include("comments.urls")
    ),
]
