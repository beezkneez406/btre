from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


# Create your views here.
def index(request):
    # grab all objects from the listings model
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # create a paginator and paged_variable
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # create a context dict for passing to index template
    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    # Grab the individual listing using the listing_id
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')