from django.shortcuts import redirect, render
from django.views.generic import ListView
from . import models

# Create your views here.
class HomeView(ListView):

    """Home View Definition"""

    model = models.Room
    template_name = "rooms/home.html"
    paginate_by = 10
    paginate_orphans = 3
    page_kwarg = "page"
