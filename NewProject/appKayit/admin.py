from django.contrib import admin
from .models import Personel


class PersonelAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','isPublished')
    list_display_links = ('id','name')
    search_fields = ('name','surname')


admin.site.register(Personel, PersonelAdmin)

