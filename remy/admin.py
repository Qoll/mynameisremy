from django.contrib import admin
from import_export import resources
from .models import DataCollection
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class DataResource(resources.ModelResource):

    class Meta:
        model=DataCollection

class DataAdmin(ImportExportModelAdmin):
    resource_class=DataResource

admin.site.register(DataCollection, DataAdmin)
