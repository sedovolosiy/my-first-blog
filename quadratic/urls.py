from django.conf.urls import patterns, include, url

from quadratic import views


urlpatterns = patterns('',
    url(r'^results/', views.quadratic_results, name='quadratic_results'),
)