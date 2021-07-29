from django.urls import path
from users import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]

app_name = "users"
