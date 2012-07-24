from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template.defaultfilters import slugify
from form.models import Submission, SubmissionForm

import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import textwrap

# Create your views here.

def index(request):
	errors = []
        if request.method == 'POST':
			form = SubmissionForm(request.POST)
			if not errors and form.is_valid():
				
				unit_name = request.POST.get('unit_name')
				unit_name_slug = slugify(unit_name)
				font = ImageFont.truetype("form/static/fonts/ameri-webfont.ttf", 15) #replace 15 with font size
				
				# Let's do some stuff...
				
				muid_k = Image.open("form/static/img/muid/muid-template-rgb.png")				
				draw = ImageDraw.Draw(muid_k)
				
				draw.text((0, 0), unit_name, (0,0,0), font=font) #position, text, color, font
				draw = ImageDraw.Draw(muid_k)
				
				muid_k.save(unit_name + "-K.png")
				muid_k.save(unit_name + "-K.jpeg")
				muid_k.convert("CMYK").save(unit_name_slug + "-K.pdf")
				muid_k.convert("CMYK").save(unit_name_slug + "-K.eps")
				
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