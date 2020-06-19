from import_export import resources
from .models import DataCollection

class DataResource(resources.ModelResource):
  class Meta:
    model=DataCollection
