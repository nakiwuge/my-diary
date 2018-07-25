from v1 import app
import unittest
import json

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        self.data=  {"id":"1","content":"i learnt thow to make templates","date":"25-july-2018","title": "templating"}
     
    #test get all erntries end point  
    def test_get_all_enteries(self):
        response = self.tester.get('/api/v1/entries', data=self.data)
        self.assertEqual(response.status_code, 200)

     
    #test post entry end point 
    def test_post_entery(self):
        response = self.tester.post('/api/v1/entries',data=self.data)
        self.assertEqual(response.status_code, 200)


    #test get entry_id end point
    def test_get_entry_id(self):
        response = self.tester.get('/api/v1/entries/1',data=self.data)
        self.assertEqual(response.status_code, 200)
 
       
        

if __name__ =="__main__":
    unittest.main()