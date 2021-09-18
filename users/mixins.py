from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin


class LoggedOutOnlyView(UserPassesTestMixin):
    """로그아웃인 상태인 사람만 볼 수 있다.(익명의 유저만)"""

    permission_denied_message = "Page not found"

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        """로그인된 상태일 떼 이동"""
        return redirect("core:home")
