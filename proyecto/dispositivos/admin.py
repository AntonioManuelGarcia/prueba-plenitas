from django.contrib import admin
from .models import Dispositivo

class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'ip', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'ip', 'user__email')
    raw_id_fields = ('user',)
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'

admin.site.register(Dispositivo, DispositivoAdmin)