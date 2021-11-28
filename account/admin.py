from django.contrib import admin
from account.models import Client, Doctor, Assistant

# Register your models here.

admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Assistant)
