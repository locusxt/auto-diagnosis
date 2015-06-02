from django.conf.urls import patterns, url
from diagnosis import views

urlpatterns = patterns('',
                        url(r'^test/$', views.start_diagnosis, name='test'),
                        url(r'^test/ajax/get_states/$', views.get_states),
                        url(r'^test/ajax/get_modules/$', views.get_modules),
                        url(r'^test/ajax/get_module_questions/$', views.get_module_questions),
                        url(r'^test/ajax/get_res/$', views.get_res),
                        url(r'^test/ajax/get_details/$', views.get_details),
                        url(r'^test/ajax/get_disease_questions/$', views.get_disease_questions),
                        url(r'^test/ajax/get_treatment/$', views.get_treatment),
)
