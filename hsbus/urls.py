from django.conf.urls import url
from . import views

app_name = 'hsbus'
urlpatterns=[
    url(r'^$', views.home, name='home'),
    # url(r'^buslog/(?P<subtitle>.+)$', views.buslog),
    url(r'^buslog/marey/$', views.buslog_marey),
    url(r'^buslog/stop_compliance/$', views.buslog_stop_compliance),
    url(r'^buslog/station_stop/$', views.buslog_station_stop),
    url(r'^passenger/route/$', views.passenger_route),
    url(r'^passenger/route_station/$', views.passenger_route_station),
    url(r'^passenger/pattern_total/$', views.passenger_pattern_total),
    url(r'^passenger/pattern_commute/$', views.passenger_pattern_commute),

]
