from django.urls import path
from rooms import views as room_views

urlpatterns = [
    path("<int:pk>/", room_views.room_details, name="details"),
    path("<int:pk>/edit/", room_views.EditRoomView.as_view(), name="edit"),
    path("<int:pk>/photos/", room_views.RoomPhotosView.as_view(), name="photos"),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/delete/",
        room_views.delete_photo,
        name="delete-photo",
    ),
    path(
        "<int:room_pk>/photos/<int:photo_pk>/edit/",
        room_views.EditPhotoView.as_view(),
        name="edit-photo",
    ),
    path("<int:pk>/photos/add", room_views.AddPhotoView.as_view(), name="add-photo"),
    path("search/", room_views.SearchView.as_view(), name="search"),
]

app_name = "rooms"
