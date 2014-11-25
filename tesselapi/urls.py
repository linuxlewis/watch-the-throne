from rest_framework import routers

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from events.views import EnvironmentEventViewSet
from throne.views import BathroomViewSet, UiView, BathroomAlertViewSet



router = routers.SimpleRouter()
router.register(r'events', EnvironmentEventViewSet)
router.register(r'bathrooms', BathroomViewSet)
router.register(r'bathroomalerts', BathroomAlertViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tesselapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', UiView.as_view(), name='index')
) + staticfiles_urlpatterns()
