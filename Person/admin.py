from django.contrib import admin
from .models import Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    search_fields=('email',)
admin.site.register(Person,PersonAdmin)