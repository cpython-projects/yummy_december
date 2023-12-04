from django.contrib import admin
from .models import MainMenuItems, Footer


@admin.register(MainMenuItems)
class MainMenuItemsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'is_anchor', 'is_visible', 'order')
    list_editable = ('is_anchor', 'is_visible', 'order')

admin.site.register(Footer)


