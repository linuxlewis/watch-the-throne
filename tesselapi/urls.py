from rest_framework import routers

from django.conf.urls import patterns, include, url
from django.contrib import admin

from events.views import EnvironmentEventViewSet



router = routers.SimpleRouter()
router.register(r'events', EnvironmentEventViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tesselapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
