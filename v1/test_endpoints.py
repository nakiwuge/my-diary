from v1 import app
import unittest
import json

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        self.data=  {"content": "i learnt thow to make templates","date": "25-july-2018","id": 7,"title": "templathiahijing"}
     
       
    def test_get_results_from_all_enteries(self):
        response = self.tester.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)


       
        

if __name__ =="__main__":
    unittest.main()