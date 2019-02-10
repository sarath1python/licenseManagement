from django.contrib import admin

from .models import License, Violation


class ViolationAdmin(admin.StackedInline):
    model = Violation
    exclude = ('updated_by',)


class LicenceeAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'mobile_number', 'number', 'status', 'issued_date')
    search_fields = ('number', 'name', 'serial_number')
    list_filter = ('status',)
    exclude = ('updated_by',)
    inlines = [
        ViolationAdmin,
    ]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.updated_by = request.user
            instance.save()
        formset.save_m2m()


admin.site.register(License, LicenceeAdmin)
