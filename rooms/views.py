from django.http.response import Http404
from django.utils import timezone
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.urls import reverse
from . import models

# Create your views here.
class HomeView(ListView):

    """Home View Definition"""

    # return object_lists
    model = models.Room
    template_name = "rooms/home.html"
    paginate_by = 10
    paginate_orphans = 3
    page_kwarg = "page"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        now = timezone.now()
        context = super().get_context_data(**kwargs)
        context["now"] = now
        return context


def room_details(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/room_details.html", {"room": room})
    except models.Room.DoesNotExist:
        # return redirect("/")
        # return redirect(reverse("core:home"))
        raise Http404()
