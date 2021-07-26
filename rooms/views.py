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
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    s_room_type = int(request.GET.get("room_type", 0))
    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    beds = int(request.GET.get("beds", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    baths = int(request.GET.get("baths", 0))
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    room_types = models.Room.objects.all()
    s_amenities = request.GET.getlist("amenities")
    s_facilities = request.GET.getlist("facilities")
    superhost = bool(request.GET.get("superhost", False))
    instant = bool(request.GET.get("instant", False))

    filter_args = {}

    filter_args["country"] = country

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args["price__lte"] = price
    if guests != 0:
        filter_args["guests__gte"] = guests
    if beds != 0:
        filter_args["beds__gte"] = beds
    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms
    if baths != 0:
        filter_args["baths__gte"] = baths
    if instant is True:
        filter_args["instant_book"] = True
    if superhost is True:
        filter_args["host__superhost"] = True
    rooms = models.Room.objects.filter(**filter_args)
    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            rooms = rooms.filter(amenities__pk=int(s_amenity))
    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["facilities__pk"] = int(s_facility)
    form = {
        "city": city,
        "countries": countries,
        "room_type": room_type,
        "price": price,
        "guests": guests,
        "beds": beds,
        "bedrooms": bedrooms,
        "baths": baths,
        "superhost": superhost,
        "instant": instant,
    }
    choice = {
        "s_room_type": s_room_type,
        "s_country": country,
        "amenities": amenities,
        "room_types": room_types,
        "facilities": facilities,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
    }
    return render(
        request,
        "search.html",
        {**form, **choice, "rooms": rooms},
    )
