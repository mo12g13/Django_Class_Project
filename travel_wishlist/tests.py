from django.test import TestCase
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



