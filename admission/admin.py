from django.contrib import admin
from .models import Admission
# Register your models here.
class AdmissionAdmin(admin.ModelAdmin):
    list_display=('id','stu_name','stu_father','joindate','stu_class','fees')
admin.site.register(Admission,AdmissionAdmin)