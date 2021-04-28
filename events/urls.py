
from django.urls import path,include
from . import views


urlpatterns = [
    #path converters
    #int: numbers
    #str: strings
    #path:whole urls /
    #slug: hypehn-and_underscore_stuff
    #UUID: universally unique indentifier
    path('',views.home,name="home"),
    path('<int:year>/<str:month>/',views.home,name="home"),
    path('events',views.all_events,name='events-list'),
    path('add_venue',views.add_venue,name='add-venue'),
]
