from django.contrib import admin
from service.models import Service
class employee_data(admin.ModelAdmin):
    list_display=('E_id','Name','January','February','March','April','May','June','July','August','September','October','November','December')
admin.site.register(Service,employee_data)