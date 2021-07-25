from django.http.response import Http404
from django.utils import timezone
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.urls import reverse
from django_countries import countries

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


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    s_room_type = int(request.GET.get("room_type", 0))
    s_country = request.GET.get("country")
    form = {"city": city, "countries": countries, "room_types": room_types}
    choice = {"s_room_type": s_room_type, "s_country": s_country}
    return render(request, "search.html", {**form, **choice})
