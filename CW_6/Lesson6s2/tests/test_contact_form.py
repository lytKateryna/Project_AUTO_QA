from time import sleep
from .base_test import BaseTest
from .test_data import USERNAME, PASSWORD
class TestContactForm(BaseTest):

    def test_successful_open(self):
       self.contact_page.open()
       sleep(1)