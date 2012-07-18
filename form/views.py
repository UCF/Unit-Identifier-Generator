from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import RequestContext
from form.models import Submission, Logo, SubmissionForm

# Create your views here.

def index(request):
	p = get_object_or_404(Submission)
	return render_to_response('form/index.html', context_instance=RequestContext(request))

def submit(request):
	errors = []
        if request.method == 'POST':
			
			form = SubmissionForm(request.POST)
			
			if not request.POST.get('name', ''):
				errors.append('Please enter a unit name.')
			if not request.POST.get('requested_by', ''):
				errors.append('Please enter your name under "Requested by."')
			if not request.POST.get('phone', ''):
				errors.append('Please enter a phone number.')
			if request.POST.get('email') and '@' not in request.POST['email']:
				errors.append('Enter a valid e-mail address.')
			if not request.POST.get('department', ''):
				errors.append('Please enter the name of the department/college making this logo request.')
			if not request.POST.get('logo_type', ''):
				errors.append('Please specify which logos you would like to generate.')
			if not errors and form.is_valid():
				return HttpResponseRedirect('/download/')
        return render_to_response('form/index.html', {
			'errors': errors,
			'name': request.POST.get('name', ''),
			'requested_by': request.POST.get('requested_by', ''),
			'phone': request.POST.get('phone', ''),
			'email': request.POST.get('email', ''),
			'department': request.POST.get('department', ''),
		}, context_instance=RequestContext(request))

def download(request):
	p = get_object_or_404(Submission)
	return render_to_response('form/download.html', context_instance=RequestContext(request))