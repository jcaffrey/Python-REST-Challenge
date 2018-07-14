import os
import unittest
 
from server import app

class BasicTests(unittest.TestCase):
      # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        self.app = app.test_client()
 
    # executed after each test
    def tearDown(self):
        pass
 
    def test_ping(self):
        response = self.app.get('/ping', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', response.data)
    
    # def test_get_people(self):
    #     response = self.app.get('/people', follow_redirects=True)

    #     self.assertEqual(response.status_code, 200)
    #     print response.data
if __name__ == "__main__":
    unittest.main()