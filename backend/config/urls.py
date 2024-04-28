from dj_rest_auth.registration.views import (
    ConfirmEmailView,
    RegisterView,
    VerifyEmailView,
)
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.conf import settings
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularRedocView,
)
from woodiem.users.views import GoogleLogin


def health_check(request):
    print("health check")
    return JsonResponse({"status": "ok"})


urlpatterns = [
    path("health-check/", health_check, name="health-check"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path(
        "redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    ###
    path("user/me", UserDetailsView.as_view(), name="user-details"),
    path("api/v1/auth/account-confirm-email/<str:key>/", ConfirmEmailView.as_view()),
    path("api/v1/auth/register/", RegisterView.as_view()),
    path("api/v1/auth/login/", LoginView.as_view()),
    path("api/v1/auth/logout/", LogoutView.as_view()),
    path(
        "api/v1/auth/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"
    ),
    path(
        "api/v1/auth/account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    re_path(
        r"^api/v1/auth/account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    ## social
    path("api/v1/auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("api/v1/profiles/", include("woodiem.profiles.urls")),
    path("api/v1/articles/", include("woodiem.articles.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
