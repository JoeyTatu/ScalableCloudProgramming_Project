from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.listings, name='index'),
    path(r'listings', views.listings, name='listings'),
    path(r'profile/<int:property_id>/', views.display_property_profile, name="profile"),
]