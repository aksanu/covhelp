from django.contrib import admin
from . import models
# Register your models here.

class covidAdmin(admin.ModelAdmin):
	fieldsets = (
		('Help', {
			'fields': ('person_name','person_detail','person_mobile','hospital','state','city','service','blood_group',
				'status')
		}),
		
	)
	list_filter = ('city', 'state')
	list_per_page= 20
	search_fields = ['service']

admin.site.register(models.covidHelp,covidAdmin)