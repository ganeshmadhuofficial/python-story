from django.contrib import admin
from .models import Line

class LineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Line, LineAdmin)