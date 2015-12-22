from django.conf.urls import patterns, url

from coaches import views

urlpatterns = patterns('',
    url(r'^(?P<coaid>\d+)/$', views.detail, name='detail'),
    
)