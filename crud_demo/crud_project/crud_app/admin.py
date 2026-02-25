from django.contrib import admin
from crud_app.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['sno', 'sname', 'sclass', 'saddress']

admin.site.register(Student, StudentAdmin)
#1234