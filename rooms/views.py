from math import ceil
from django.shortcuts import render
from . import models

# Create your views here.
def all_rooms(request):
    page = int(request.GET.get("page", 1) or 1)
    page_size = 10
    limit = page * page_size
    start = page_size * (page - 1)
    all_rooms = models.Room.objects.all()[start:limit]
    page_count = ceil(models.Room.objects.count() / page_size)
    page_range = range(1, page_count + 1)
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": page_range,
        },
    )
