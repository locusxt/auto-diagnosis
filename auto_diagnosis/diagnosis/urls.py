from django.conf.urls import patterns, url
from diagnosis import views

urlpatterns = patterns('',
                        url(r'^test/$', views.start_diagnosis, name='test'),
)
