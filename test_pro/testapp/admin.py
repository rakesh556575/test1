from django.contrib import admin
from testapp.models import Testcases
# Register your models here.

class TestcasesAdmin(admin.ModelAdmin):
    list_display = ["testid","testname","testcategory"]


admin.site.register(Testcases,TestcasesAdmin)