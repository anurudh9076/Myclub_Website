from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event,Venue
from .forms import VenueForm,EventForm

# Create your views here.
def update_event(request,event_id):
    event=Event.objects.get(pk=event_id)  
    form = EventForm(request.POST or None,instance=event)
    if form.is_valid():
        form.save()
        return redirect('events-list')

    return render (request,'events/update_event.html',{'form':form})

def add_event(request):
    submitted=False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted =True
    return render(request,'events/add_event.html',{'form':form,'submitted':submitted})

def update_venue(request,venue_id):
        venue=Venue.objects.get(pk=venue_id)  
        form = VenueForm(request.POST or None,instance=venue)
        if form.is_valid():
            form.save()
            return redirect('list-venue')

        return render (request,'events/update_venue.html',{'form':form})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render (request,'events/search_venues.html',{'searched':searched,'venues':venues})
    else:
        return render (request,'events/search_venues.html',{})

    
def show_venue(request,venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render (request,'events/show_venue.html',{'venue':venue})

def list_venue(request):
    venue_list = Venue.objects.all()
    return render (request,'events/venue.html',{'venue_list':venue_list})
def add_venue(request):
    submitted=False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted =True
    return render(request,'events/add_venue.html',{'form':form,'submitted':submitted})


def all_events(request):
    event_list=Event.objects.all()
    return render(request,'events/events_list.html',{'event_list':event_list})


def home(request,year=datetime.now().year,month=datetime.now().strftime('%B')):
    name="anir"
    #convert month from name to number
    month=month.capitalize()
    
    month_number =  list(calendar.month_name).index(month)
    month_number=int(month_number)
    cal=HTMLCalendar().formatmonth(year,month_number)
    #get current year
    now=datetime.now()
    current_year= now.year
    #get current time
    time=now.strftime('%I:%M:%S %p')
    return render(request,'events/home.html',
                        {'name':name,
                        'year':year,
                        'month':month,
                        'month_number':month_number,
                        'cal':cal,
                        'current_year':current_year,
                        'time':time})

