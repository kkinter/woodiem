from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


class CustomGoogleOAuth2Adapter(GoogleOAuth2Adapter):
    def complete_login(self, request, app, token, **kwargs):
        print("complete_login")
        return super().complete_login(request, app, token, **kwargs)


class GoogleLogin(SocialLoginView):
    adapter_class = CustomGoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://localhost:8000/accounts/google/login/callback/"

    def dispatch(self, *args, **kwargs):
        print(self.request)
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(self.request)
        return super().post(request, *args, **kwargs)

    def process_login(self):
        print("hi")
        return super().process_login()
