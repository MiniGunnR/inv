from django.contrib import admin

from .models import LC, LCItem


class LCItemInline(admin.TabularInline):
    model = LCItem
    extra = 1


class LCAdmin(admin.ModelAdmin):
    inlines = [
        LCItemInline,
    ]

admin.site.register(LC, LCAdmin)
