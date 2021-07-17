from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page")
    room_lists = models.Room.objects.all()
    paginator = Paginator(room_lists, 10)
    rooms = paginator.get_page(page)
    return render(
        request,
        "rooms/home.html",
        {"rooms": rooms},
    )
