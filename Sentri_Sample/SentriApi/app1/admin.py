from django.contrib import admin
from app1.models import Emissions


@admin.register(Emissions)
class EmissionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'accounting_period', 'scope_1', 'scope_2', 'scope_3']
    search_fields = ['accounting_period',]
    list_filter = ['accounting_period',]
