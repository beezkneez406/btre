from django.shortcuts import render
from .models import Listing


# Create your views here.
def index(request):
    # grab all objects from the listings model
    listings = Listing.objects.all()
    # create a context dict for passing to index template
    context = {
        'listings': listings,
        'name': 'Jake'
    }
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')