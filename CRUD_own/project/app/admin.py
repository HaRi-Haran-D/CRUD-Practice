from django.contrib import admin
from .models import Company

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("emp_id", "emp_name", "occupation", "salary", "joining_date")
    search_fields = ("emp_name", "occupation")
    list_filter = ("occupation", "joining_date")