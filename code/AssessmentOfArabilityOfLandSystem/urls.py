from django.conf.urls import include, url
from django.contrib import admin
from System import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'AssessmentOfArabilityOfLandSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^index/(?P<err_mess>\w+)/$', views.index_err_mess),
    url(r'^info-input$', views.info_input),
    url(r'^file-upload$', views.file_upload),
    url(r'^analyse$', views.analyse),
    url(r'^admin/', include(admin.site.urls)),
]
