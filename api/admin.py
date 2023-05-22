from django.contrib import admin
from .models import Culprit
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CulpritResource(resources.ModelResource):
    class Meta:
       model = Culprit

class CulpritAdmin(ImportExportModelAdmin):
    resource_classes = [CulpritResource]

# Register your models here.
admin.site.register(Culprit, CulpritAdmin)

#admin.site.register(Culprit)