from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'hsbus/home.html')

def buslog_marey(request):
    return render(request, 'hsbus/buslog_marey.html')

def buslog_stop_compliance(request):
    return render(request, 'hsbus/buslog_stop_compliance.html')

def buslog_station_stop(request):
    return render(request, "hsbus/buslog_station_stop.html")

def passenger_route(request):
    return render(request,"hsbus/passenger_route.html")

def passenger_route_station(request):
    return render(request,"hsbus/passenger_route_station.html")

def passenger_pattern_total(request):
    return render(request,"hsbus/passenger_pattern_total.html")

def passenger_pattern_commute(request):
    return render(request,"hsbus/passenger_pattern_commute.html")