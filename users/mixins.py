from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy


class EmailLoginOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, "Can't go there")
        return redirect("core:home")


class LoggedOutOnlyView(UserPassesTestMixin):
    """로그아웃인 상태인 사람만 볼 수 있다.(익명의 유저만)"""

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        """로그인된 상태일 떼 이동"""
        messages.error(self.request, "Can't go there")
        return redirect("core:home")


class LoggedinOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")
