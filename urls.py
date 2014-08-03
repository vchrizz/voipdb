from django.conf.urls.defaults import patterns, include, url
#from voip import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voipdb.views.home', name='home'),
    # url(r'^voipdb/', include('voipdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('voip.urls')),

#    # ex: /
#    url(r'^$', views.index, name='index'),
#    # ex: /
#    #url(r'^login$', views.login_user, name='login_user'),
#
#    url(r'^login/$', 'django.contrib.auth.views.login', {
#      'template_name': 'voip/templates/voip/login.html'
#    }),
#    url(r'^logout/$', 'django.contrib.auth.views.logout', {
#      #'template_name': 'admin/login.html'
#    }),
#
#    # ex: /extensions/
#    url(r'^extensions/$', views.extension_show, name='extension_show'),
#
#    # ex: /extensions/5/edit/
#    url(r'^extensions/(?P<extension_id>\d+)/edit/$', views.extension_edit, name='extension_edit'),
#
#    # ex: /polls/5/vote/
##    url(r'^(?P<member_id>\d+)/vote/$', views.vote, name='vote'),
)
