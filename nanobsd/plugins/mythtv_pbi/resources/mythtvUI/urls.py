from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
     url(r'^plugins/mythtv/', include('mythtvUI.freenas.urls')),
)
