from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from form.models import Submission, SubmissionForm
from form.idgen import IDGen

# Create your views here.

def index(request):
	errors = []
        if request.method == 'POST':
			form = SubmissionForm(request.POST)
			if not errors and form.is_valid():
				
				design_options = request.POST.getlist('design_options')
				unit_name = request.POST.get('unit_name')				
				
				uid_fontsize = request.POST.get('uid_fontsize')
				muid_fontsize = request.POST.get('muid_fontsize')
				vuid_fontsize = request.POST.get('vuid_fontsize')
				
				uid_spanw = request.POST.get('uid_span_w')
				muid_spanw = request.POST.get('muid_span_w')
				vuid_spanw = request.POST.get('vuid_span_w')
				
				uid_spanh = request.POST.get('uid_span_h')
				muid_spanh = request.POST.get('muid_span_h')
				vuid_spanh = request.POST.get('vuid_span_h')
				
				muid_linebreak = request.POST.get('muid_linebreak')
				
				# From here, need to run process only for each selected design option...
				
				# IDGen() takes 6 args: design_option, unit_name, fontsize, spanw, spanh, muid_linebreak
				
				#if 'UID' in design_options:
					# Do the UID stuff...
				#if 'MUID' in design_options:
					# Do the MUID stuff...
				
				muidgen = IDGen("MUID", unit_name, muid_fontsize, muid_spanw, muid_spanh, muid_linebreak)
				muidgen.makelogos()
					
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