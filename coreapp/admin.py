from django.contrib import admin
from coreapp.models import employers


class employersAdmin(admin.ModelAdmin):
    class Meta:
        model = employers
admin.site.register(employers,employersAdmin)
               

