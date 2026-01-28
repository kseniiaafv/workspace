from django.contrib import admin
from django.utils.html import mark_safe
from .models import Dog
from .models import (
    SiteSettings,
    Specialist,
    Review,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "updated_at")

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'preview_photo', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'role', 'breed')

    def preview_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50" height="50" style="object-fit: cover; border-radius: 50%" />')
        return "-"
    preview_photo.short_description = "Фото"

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed', 'specialist', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'breed')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Колонки, видимые в списке
    list_display = ('name', 'category', 'rating', 'age_info', 'is_active', 'created_at')

    # Фильтры справа (удобно сортировать по типу отзыва)
    list_filter = ('category', 'rating', 'is_active')

    # Можно менять галочку "показывать" прямо из списка
    list_editable = ('is_active',)

    # Поиск по имени и тексту
    search_fields = ('name', 'text')

    # Порядок полей внутри карточки редактирования
    fields = ('is_active', 'category', 'name', 'age_info', 'rating', 'text')