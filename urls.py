from django.conf.urls.defaults import patterns, include, url
from portfolio import views
from django.views.static import * 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'portfolio.views.about'),
	url(r'^about/$', 'portfolio.views.about'),
	url(r'^projects/$', 'portfolio.views.projects'),
	url(r'^contact/$', 'portfolio.views.contact'),
	url(r'^projects/tixbayarea/$', 'portfolio.views.tixbayarea'),
	url(r'^projects/meta4explorer/$', 'portfolio.views.meta4explorer'),
	url(r'^projects/personalportfolio/$', 'portfolio.views.personalportfolio'),
	url(r'^projects/graphicdesign/$', 'portfolio.views.graphicdesign'),
	
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	
	#url(r'^alpha/about/$', 'portfolio.views.alpha_about')
	#url(r'^alpha/projects/$', 'portfolio.views.alpha_projects'),
	#url(r'^alpha/contact/$', 'portfolio.views.alpha_contact'),
	
	#url(r'^beta/about/$', 'portfolio.views.beta_about')
	#url(r'^beta/projects/$', 'portfolio.views.beta_projects'),
	#url(r'^beta/contact/$', 'portfolio.views.beta_contact'),
	
	#url(r'^gamma/about/$', 'portfolio.views.gamma_about')
	#url(r'^gamma/projects/$', 'portfolio.views.gamma_projects'),
	#url(r'^gamma/contact/$', 'portfolio.views.gamma_contact'),
    
	# Examples:
    # url(r'^$', 'christinaguo.views.home', name='home'),
    # url(r'^christinaguo/', include('christinaguo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
