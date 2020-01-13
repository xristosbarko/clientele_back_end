from rest_framework.filters import BaseFilterBackend
import coreapi

class AdvancedSearchFilter(BaseFilterBackend):
	def get_schema_fields(self, view):
		params = ['client', 'date_from', 'date_to', 'department', 'ip']
		QueryParameters = []
		for param in params:
			QueryParameters.append(coreapi.Field(name=param, required=False, location='query'))
		return QueryParameters