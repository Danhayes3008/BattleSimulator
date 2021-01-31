from django.shortcuts import render
from simulator.forms import *

# Create your views here.
def index(request):

    war = Warship.objects.all()
    return render(request, 'index.html', {'warship': war})