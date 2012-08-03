from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from form.models import Submission, SubmissionForm
from form.idgen import IDGen
from django.template.defaultfilters import slugify
from django.core.exceptions import ObjectDoesNotExist

from time import gmtime, strftime
import os

# Create your views here.

def index(request):
	errors = []
	match_data = 'n/a'
	match_exists_error = False
	match_requester = ''
	match_requester_dept = ''
        if request.method == 'POST':
			form = SubmissionForm(request.POST)
			if not errors and form.is_valid():
				
				requested_unit_name = request.POST.get('unit_name')
				
				try:
					match_attempt = Submission.objects.filter(unit_name=requested_unit_name).exists()
				except ObjectDoesNotExist:
					match_attempt = ''
				
				if match_attempt != False:
					match_exists_error = True
					match_data = Submission.objects.get(unit_name=requested_unit_name)
					match_requester = match_data.requester
					match_requester_dept = match_data.department
				else:
					design_options = request.POST.getlist('design_options')			
				
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
				
					# Designate the file path at which new logos will be saved.
					# e.g.: generated_logos/my-unit-name-1269884900480978/MUID/MUID-my-unit-name-K.png
				
					currenttime = strftime("%Y%m%d%H%M%S", gmtime())
				
					generated_logos_dir = settings.PROJECT_FOLDER + "/generated_logos/" + slugify(requested_unit_name) + "-" + currenttime + "/"
					if not os.path.exists(generated_logos_dir):
						os.makedirs(generated_logos_dir)
				
					# From here, need to run process only for each selected design option...
				
					# IDGen() takes up to 7 args: 
					# design_option, generated_logos_dir, unit_name, fontsize, spanw, spanh, muid_linebreak (optional-muid only)
				
					if 'UID' in design_options:
						uid_gen = IDGen("UID", generated_logos_dir, requested_unit_name, uid_fontsize, uid_spanw, uid_spanh)
						uid_gen.makelogos()
					
					if 'MUID' in design_options:				
						muid_gen = IDGen("MUID", generated_logos_dir, requested_unit_name, muid_fontsize, muid_spanw, muid_spanh, muid_linebreak)
						muid_gen.makelogos()
					
					if 'VUID' in design_options:
						vuid_gen = IDGen("VUID", generated_logos_dir, requested_unit_name, vuid_fontsize, vuid_spanw, vuid_spanh)
						vuid_gen.makelogos()
				
					form.save()
					return render_to_response('form/download.html', {
						'design_options': design_options
					}, context_instance=RequestContext(request))
	else:
		form = SubmissionForm()
		
	return render_to_response('form/index.html', {
		'form': form,
		'errors': errors,
		'match_exists_error': match_exists_error,
		'match_data': match_data,
		'match_requester': match_requester,
		'match_requester_dept': match_requester_dept,
		'name': request.POST.get('name', ''),
		'requested_by': request.POST.get('requested_by', ''),
		'phone': request.POST.get('phone', ''),
		'email': request.POST.get('email', ''),
		'department': request.POST.get('department', ''),
	}, context_instance=RequestContext(request))

def download(request):
	return render_to_response('form/download.html', context_instance=RequestContext(request))