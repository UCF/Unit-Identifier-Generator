from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from form.models import Submission

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        CreateView.as_view(
            model=Submission,
            template_name='form/index.html')),
	url(r'^download/$',
		CreateView.as_view(
			model=Submission,
			template_name='form/download.html')),
	url(r'^admin/', include(admin.site.urls)),
)