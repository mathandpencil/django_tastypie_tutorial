from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from tastypie import api
from apps.accounts import resources as account_resources

admin.autodiscover()

urlpatterns = patterns('',
    
	url(r'^$', 'apps.accounts.views.index', name='index'),
	

    url(r'^admin/', include(admin.site.urls)),
)


v1_api = api.Api(api_name='v1')
v1_api.register(account_resources.UserResource())

urlpatterns += patterns('', (r'^api/', include(v1_api.urls)))

if settings.DEBUG:
	urlpatterns += patterns('',
	    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': settings.MEDIA_ROOT}),
	)
	urlpatterns += patterns('',
	    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
	        {'document_root': settings.STATIC_ROOT}),
	)


