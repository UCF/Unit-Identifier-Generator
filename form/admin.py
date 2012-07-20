from form.models import Submission#, Logo
from django.contrib import admin

class SubmissionAdmin(admin.ModelAdmin):
	fields = ['unit_name', 'request_date', 'requester', 'phone', 'email', 'department', 'design_options']
	date_hierarchy = 'request_date'
	list_filter = ['request_date']
	list_display = ('unit_name', 'request_date', 'requester')

admin.site.register(Submission, SubmissionAdmin)
#admin.site.register(Logo)