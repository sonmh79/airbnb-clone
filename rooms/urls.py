from django.urls import path
from rooms import views as room_views

urlpatterns = [
    path("<int:pk>", room_views.room_details, name="details"),
    path("search", room_views.search, name="search"),
]

app_name = "rooms"
