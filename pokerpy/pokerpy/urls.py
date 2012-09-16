from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('tuto.views',
    url(r'^$', 'index'),
    url(r'^maospoker','maospoker'),
    url(r'^regrasgerais','regrasgerais')
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
