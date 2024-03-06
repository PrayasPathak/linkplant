from django.contrib import admin
from .models import Profile, Link

# Register your models here.


class NameFilter(admin.SimpleListFilter):
    title = "name"
    parameter_name = "name"
    ASC = "asc"
    DESC = "desc"

    def lookups(self, request, model_admin):
        return [(self.ASC, "Asc"), (self.DESC, "Desc")]

    def queryset(self, request, queryset):
        if self.value() == self.ASC:
            return queryset.order_by("name")
        else:
            return queryset.order_by("-name")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "bg_color"]
    list_per_page = 20
    list_filter = ["id", NameFilter]
    list_editable = ["bg_color"]
    prepopulated_fields = {
        "slug": ["name"],
    }
    search_fields = ["name"]


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["text", "profile", "url"]
    list_search = ["profile"]
    list_per_page = 20
