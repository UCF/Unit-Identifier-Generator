from django.conf.urls import patterns, include, url
from django.views.generic import CreateView
from form.models import Request

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        CreateView.as_view(
            model=Request,
            template_name='form/index.html')),
	url(r'^admin/', include(admin.site.urls)),
)