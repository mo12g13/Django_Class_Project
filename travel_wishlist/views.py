from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, PlaceVisitedForm


# Create your views here.
def place_list(request):

    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')

    places = Place.objects.all()
    form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'form': form})


def place_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})


def post_new_page(request, pk):

    place = get_object_or_404(Place, pk=pk)

    if request.method == "POST":
        form = PlaceVisitedForm(request.POST, instance=place)

        if form.is_valid():
            form.save()
            return redirect('place_visited')

    # Else, this is a get request. (or the form validation failed.
    #Create new form, and show the placepage.
    form = PlaceVisitedForm(instance=place) # Populate the form with data about this place
    return render(request, 'travel_wishlist/placepage.html', {'place':place, 'form': form })


def place_is_visited(request):
    if request.method == 'POST':

        pk = request.POST.get('pk')
        # place = Place.objects.get(pk=pk)
        place = get_object_or_404(Place, pk=pk)
        place.visited = True
        place.save()

    return redirect('place_list')
