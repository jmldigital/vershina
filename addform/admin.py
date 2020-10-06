from django.contrib import admin
from .models import *




class CustomerAdmin (admin.ModelAdmin):


    list_display = [field.name for field in Customers._meta.fields if field.name != "customer_smms"]
    # list_display = ["customer_fio", "purchase_detail_type","purchase_detail","customer_phone", "customer_post"]
    list_filter = ['customer_fio',]
    search_fields = ["customer_fio"]
    exclude = ["customer_smms"]  # скрыли в редкторе


admin.site.register(Customers,CustomerAdmin)
