from django.conf.urls import include, url
from django.contrib import admin
from System import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'AssessmentOfArabilityOfLandSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^infoinput$', views.infoinput),
    url(r'^analyse$', views.analyse),
    url(r'^admin/', include(admin.site.urls)),
]
