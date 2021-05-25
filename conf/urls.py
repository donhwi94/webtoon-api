from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from webtoons import views

schema_view = get_schema_view(
    openapi.Info(
        title="webtoon API",
        default_version="v1",
        description="naver webtoon 어플리케이션 주요 기능의 요구사항을 분석하여 만든 webtoon API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="test", email="test@test.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", views.api_root),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
    path("v1.0/webtoons/", include("webtoons.urls")),
    path("v1.0/interests/", include("interests.urls")),
]

urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
