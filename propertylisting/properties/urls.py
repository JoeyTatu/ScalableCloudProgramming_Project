from django.conf.urls import url

from . import views

app_name = 'properties'

urlpatterns = [
    #url('', views.listing, name='index'),
    url(r'^listings', views.listings, name='listings'),
    url(r'^profile/(?P<property_id>[0-9]+)/$', views.display_property_profile, name="profile"),
]