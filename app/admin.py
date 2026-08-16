from django.contrib import admin
from . import models
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug",)
    search_fields = ("name","slug",)
    prepopulated_fields = {"slug": ("name",),}
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","category","price","discount_price","stock","is_active","created_at","updated_at",)

    list_filter = ("category","is_active","created_at",)

    search_fields = ("name","description","category__name",)
    list_editable = ("price","discount_price","stock","is_active",)

    readonly_fields = ("created_at","updated_at",)
ordering = ("-created_at",)