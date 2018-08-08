import unittest
from django.test import Client
from django.urls import reverse


class TestBirthdayTracker(unittest.TestCase):
    def setup(self):
        self.client = Client()
    
    def tearDown(self):
        pass

    def test_save(self):
        url = reverse('save_new')
        response = self.client.post(url, data={'bday_name':'Natasha Liu', 'bday_date':'11-16',})
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()