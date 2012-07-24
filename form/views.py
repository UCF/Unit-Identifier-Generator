from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from form.models import Submission, SubmissionForm

from PIL import Image
from PIL import ImageDraw

# Create your views here.

def index(request):
	errors = []
        if request.method == 'POST':
			form = SubmissionForm(request.POST)
			if not errors and form.is_valid():
				# Let's do some stuff...
				
				img=Image.new("RGBA", (200,200),(120,20,20))
				draw = ImageDraw.Draw(img)
				img.save("a_test.png")
				
				form.save()
				return HttpResponseRedirect('/download/')	
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