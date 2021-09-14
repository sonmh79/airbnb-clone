from django.urls import path
from users import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("login/kakao", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback", views.kakao_callback, name="kakao-callback"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]

app_name = "users"
