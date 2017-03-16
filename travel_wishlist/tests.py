from django.test import TestCase, LiveServerTestCase
from django.core.urlresolvers import reverse
from .models import Place


# Create your tests here.

class TestViewHomePageIsEmptyList(TestCase):
    def test_load_home_page_shows_empy_list(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places'])

class TwinWishList(TestCase):

    #Load this into the database for all the test
    fixtures = ['test_places']


    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        #Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        # What data was sent to the template
        data_rendered = list(response.context['places'])

        #What data is in the database? Get all of the items where visited=False
        data_expected = list(Place.objects.filter(visited=False))

        self.assertCountEqual(data_rendered, data_expected)


    def test_view_places_visited(self):
        """Checking the response to see which data was sent to the template"""
        response = self.client.get(reverse('place_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')
        # What data was sent to the template?
        data_rendered = list(response.context['visited'])
        data_expected = list(Place.objects.filter(visited=True))

        self.assertCountEqual(data_rendered, data_expected)

class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place_to_wishlist(self):

        response =  self.client.post(reverse('place_list'), { 'name': 'Tokyo', 'visited': False}, follow=True)

        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Populate the response of the for this place
        response_places = response.context['places']

        self.assertEqual(len(response_places), 1)
        tokyo_response = response_places[0]


        # Checking if a data is in a database and the place has been visited
        tokyo_in_database = Place.objects.get(name="Tokyo", visited=False)

        self.assertEqual(tokyo_response, tokyo_in_database)
        response =  self.client.post(reverse('place_list'), { 'name': 'Yosemite', 'visited': False}, follow=True)
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        response_places = response.context['places']
        self.assertEqual(len(response_places), 2)

        place_in_database = Place.objects.get(name="Yosemite", visited=False)
        place_in_database = Place.objects.get(name="Tokyo", visited=False)

        places_in_database = Place.objects.all()  # Get all data

        self.assertCountEqual(list(places_in_database), list(response_places))

    # Testing of the add places to see if it works
    def test_add_new_visited_place_to_wishlist(self):

        response =  self.client.post(reverse('place_list'), { 'name': 'Tokyo', 'visited': True}, follow=True)

        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # What data was used to populate the template?
        response_places = response.context['places']
        # Should be 0 items - have not added any un-visited places
        self.assertEqual(len(response_places), 0)
        place_in_database = Place.objects.get(name="Tokyo", visited=True)






