from django.contrib import admin
from .models import SavedText

class SavedTextAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at", "text"]
    class Meta:
        model = SavedText

admin.site.register(SavedText, SavedTextAdmin)
