from django.contrib import admin

from storage.models import *
# Register your models here.

admin.site.register(Tag)
admin.site.register(Storage)
admin.site.register(Object)
admin.site.register(Collection)