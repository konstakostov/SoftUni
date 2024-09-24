from django.contrib import admin

from djangoUrlsAndViews.departments.models import Department


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass