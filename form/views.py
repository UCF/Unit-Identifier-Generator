from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template.defaultfilters import slugify
from form.models import Submission, SubmissionForm
from form.idgen import IDGen

# Create your views here.

def index(request):
	errors = []
        if request.method == 'POST':
			form = SubmissionForm(request.POST)
			if not errors and form.is_valid():
				
				unit_name = request.POST.get('unit_name')
				unit_name_slug = slugify(unit_name)
				unit_name_caps = unit_name.upper()
				
				design_options = request.POST.getlist('design_options')
				
				# From here, need to run process only for each selected design option...
				
				#if 'UID' in design_options:
					# Do the UID stuff...
				#if 'MUID' in design_options:
					# Do the MUID stuff...
				
				muidgen = IDGen("MUID", unit_name_caps, unit_name_slug)
				muidgen.temporaryrun()
					
				#if 'VUID' in design_options:
					# Do the VUID stuff...
				
				form.save()
				return render_to_response('form/download.html', {
					'design_options': design_options
				}, context_instance=RequestContext(request))
	else:
		form = SubmissionForm()
		
	return render_to_response('form/index.html', {
		'form': form,
		'errors': errors,
		'name': request.POST.get('name', ''),
		'requested_by': request.POST.get('requested_by', ''),
		'phone': request.POST.get('phone', ''),
		'email': request.POST.get('email', ''),
		'department': request.POST.get('department', ''),
	}, context_instance=RequestContext(request))

def download(request):
	return render_to_response('form/download.html', context_instance=RequestContext(request))