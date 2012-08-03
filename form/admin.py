from django.forms import ModelForm
from django.contrib import admin
from form.models import Submission

class SubmissionAdmin(admin.ModelAdmin):
	fields = ['unit_name', 'request_date', 'requester', 'phone', 'email', 'department', 'design_options', 'comments']
	date_hierarchy = 'request_date'
	ordering = ['-request_date']
	list_filter = ['request_date']
	list_display = ('unit_name', 'request_date', 'requester', 'comments')
	readonly_fields = ('comments',)
	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['comments']
		else:
			return []
	

admin.site.register(Submission, SubmissionAdmin)