from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)

urlpatterns = [
#	url(r'^$', 'qa.404.notfound', name='ask-home'),
	url(r'^', include('qa.urls')),
]
