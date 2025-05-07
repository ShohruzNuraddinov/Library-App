from django.urls import path


from apps.users.api_endpoints import *

app_name = 'users'

urlpatterns = [
    path("signup/", SignupAPIView.as_view(), name="signup"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("me/", ProfileAPIView.as_view(), name="profile"),
]
