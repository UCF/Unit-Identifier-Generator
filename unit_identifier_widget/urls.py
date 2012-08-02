from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from form.models import Submission

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'form.views.index'),
	url(r'^download/$', 'form.views.download'),
	url(r'^admin/', include(admin.site.urls)),
)