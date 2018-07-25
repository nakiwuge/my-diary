from v1 import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self) 
        self.data ={"id":"3","title":"add","content":"content", "date":"date"} 

    #testing get entries url 
    def test_get_all_enteries_url_with_data(self):
        response = self.tester.get('/api/v1/entries', data=self.data)
        self.assertEqual(self.data, response.data)
    def test_get_all_enteries_urla(self):
        response = self.tester.get('/api/v1/entries')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"no entries added, please add an entry", response.data)

    #testing post entries url
    def test_post_enrty(self):
        response = self.tester.post('/api/v1/entries')
        if response.data==self.data:
            self.assertEqual(response.status_code, 200)
        
    #test if invalid key error is returned 
    def test_invalid_entry_post(self):
        response = self.tester.post('/api/v1/entries')
        if response.data=="":
            self.assertIn(b"key should either be id ,content ,date and title", response.data)

    #test if database is empty error exists
    def test_for_no_entries_error_for_entryid(self):
        response = self.tester.get('/api/v1/entries/entryid')
        if response.data=="":
           self.assertEqual(response.status_code, 200)
    #test if invalid id error exists
    def test_for_put_method(self):
        response = self.tester.put('/api/v1/entries/entryid')
        if response.data=="":
           self.assertEqual(response.status_code, 200)
       
        

if __name__ =="__main__":
    unittest.main()