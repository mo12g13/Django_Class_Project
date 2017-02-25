import selenium

from selenium import webdriver
from django.test import  LiveServerTestCase

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
import  time




class PageViewTest(LiveServerTestCase):
    fixtures = ['test_places']
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait((3))

    def tearDown(self):
        self.browser.quit()

    def test_get_home_page_list_of_places(self):
        self.browser.get(self.live_server_url)
        assert 'Wishlist' in self.browser.title
        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source
        assert 'San Francisco' not in self.browser.page_source
        assert 'Moab' not in self.browser.page_source

    def test_get_list_visited_places(self):
        self.browser.get(self.live_server_url + '/visited')
        assert 'Wishlist' in self.browser.title
        assert 'Tokyo' not in self.browser.page_source
        assert 'New York' not in self.browser.page_source
        assert 'Moab' in self.browser.page_source

class FunctionalityTests(LiveServerTestCase):

    fixtures = ['test_places']

    def setUp(self):
        self.browser = webdriver.Firefox()  # Change to .Chrome() if using Chrome
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_new_place(self):

        self.browser.get(self.live_server_url)
        input_name = self.browser.find_element_by_id('id_name')
        input_name.send_keys('Denver')
        add_button = self.browser.find_element_by_id('add_new_place')
        add_button.click()
        wait_for_denver = self.browser.find_element_by_id('place_name_5')

        # Assert places from test_places are on page
        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source

        # And the new place
        assert 'Denver' in self.browser.page_source


    def test_mark_place_as_visited(self):

        # Load home page
        self.browser.get(self.live_server_url)

        visited_button = self.browser.find_element_by_id('visited_2')

        ny_gone = self.browser.find_element_by_id('place_name_2')

        visited_button.click()

        wait = WebDriverWait(self.browser, 3)
        ny_has_gone = wait.until(EC.invisibility_of_element_located((By.ID, 'place_name_2')))

        # Assert Tokyo is still on page
        assert 'Tokyo' in self.browser.page_source

        # But New York is not
        assert 'New York' not in self.browser.page_source

        # Load visited page
        self.browser.get(self.live_server_url + '/visited')

        # New York should be on the visited page
        assert 'New York' in self.browser.page_source

        # As well as our other visited places
        assert 'San Francisco' in self.browser.page_source
        assert 'Moab' in self.browser.page_source