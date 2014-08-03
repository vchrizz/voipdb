from django.conf.urls.defaults import patterns, include, url
from voip import views

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
#    url(r'^admin/', include(admin.site.urls)),

    # ex: /
    url(r'^$', views.index, name='index'),

    # ex: /userinfo/
    url(r'^userinfo/$', views.userinfo, name='userinfo'),

    # ex: /phonebook/
    url(r'^phonebook/$', views.phonebook, name='phonebook'),

    # ex: /login/
    #url(r'^login/$', views.login_user, name='login_user'),

    url(r'^login/$', 'django.contrib.auth.views.login', {
      'template_name': 'voip/login.html'
    }),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {
      #'template_name': 'voip/logout.html'
    }),

    # ex: /extensions/
    url(r'^extensions/$', views.extensions_show, name='extensions_show'),

    # ex: /extensions/5/add/
    url(r'^extensions/add/$', views.extension_add, name='extension_add'),

    # ex: /extensions/5/edit/
    url(r'^extensions/(?P<extension_id>\d+)/edit/$', views.extension_edit, name='extension_edit'),

    # ex: /extensions/5/delete/
    url(r'^extensions/(?P<extension_id>\d+)/delete/$', views.extension_delete, name='extension_delete'),

    # ex: /sipuser/5/add/
    url(r'^sipuser/(?P<extension_id>\d+)/add/$', views.sipuser_add, name='sipuser_add'),

    # ex: /sipuser/5/edit/
    url(r'^sipuser/(?P<sipuser_id>\d+)/edit/$', views.sipuser_edit, name='sipuser_edit'),

    # ex: /sipuser/5/delete/
    url(r'^sipuser/(?P<sipuser_id>\d+)/delete/$', views.sipuser_delete, name='sipuser_delete'),

)
