from django.contrib import admin
from .models import Company, Employee, Communication


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    search_fields = ("title",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name",)
    search_fields = ("first_name",)
    empty_value_display = "-пусто-"


class CommunicationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    empty_value_display = "-пусто-"


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Communication, CommunicationAdmin)

