from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ["name", "used_by"]

    def used_by(self, obj):
        return obj.rooms.count()

    pass


# 어드민 안에 새로운 어드민 추가(ForeignKey로 연결)
class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    # 인라인 어드민 리스트
    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Spaces",
            {
                "fields": ("amenities", "facilities", "house_rules"),
                "classes": ("collapse",),
            },
        ),
        ("More", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "host",
        "count_amenities",
        "count_photos",
        "total_rating",
    )
    ordering = ("name", "price", "bedrooms")

    list_filter = ("instant_book", "city", "country")
    search_fields = [
        "city",
        "host__username",
    ]
    filter_horizontal = ("amenities", "facilities", "house_rules")

    # 아이템이 많을 때 검색 가능
    raw_id_fields = ("host",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_amenities.short_description = "Amenities"
    count_photos.short_description = "Photo Counts"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        print(obj.file)
        return mark_safe(f'<img width="50px" src="{obj.file.url}">')

    get_thumbnail.short_description = "Thumbnail"
