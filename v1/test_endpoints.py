from v1 import app
import unittest
import json

class EntryTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self) 
        self.data = json.dumps({
            'id': '3', 
            'title': 'this',
            'content': 'this content', 
            'date': '5-6-8'}) 
        self.response = self.tester.post(
            '/api/v1/entries',
            data=self.data,
            content_type='application/json'
            )

    '''testing if database is empty'''
    def test_for_error_returned_when_no_entries(self):
        resp = self.tester.get('/api/v1/entries')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"no entries added, please add an entry", resp.data)

    '''testing the get with the data'''
    def test_success_for_get_all_entries(self):
        self.response
        response = self.tester.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    '''testing for invalid keys passed and values passed'''
    def test_for_error_returned_when_no_title_key(self):
        dummy_data = json.dumps({
            'id': '3', 
            'content': 'this',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add title and try again", 
            response.data
            )    
        
    def test_for_error_returned_when_no_title_value(self):
        dummy_data = json.dumps({
            'id': '3', 
            'title':"  ",
            'content': 'this',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add title to your entry", 
            response.data
            )

    def test_for_error_returned_when_no_content_key(self):
        dummy_data = json.dumps({
            'id': '3', 
            'title': 'this',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add content and try again", 
            response.data
            )    
        
    def test_for_error_returned_when_no_content_value(self):
        dummy_data = json.dumps({
            'id': '3', 
            'title':"this",
            'content': '',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add write something in the content", 
            response.data
            )        
    ''' tests for fetching a soecific entry'''
    def test_for_error_for_no_specified_entry(self):
        response = self.tester.get('/api/v1/entries/6')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"no entry with that id", response.data)

    def test_for_sucessfull_get_specific_entry(self):
        self.response
        response = self.tester.get('/api/v1/entries/3')
        self.assertEqual(response.status_code, 200)   
    ''' tests for validation errors when modifying entries'''
    def test_for_error_returned_when_modifying_with_no_title_key(self):
        dummy_data = json.dumps({
            'id': '3', 
            'content': 'this',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add title and try again", 
            response.data
            )    
        
    def test_for_error_returned_when_modifying_with_no_title_value(self):
        dummy_data = json.dumps({
            'id': '3', 
            'title':"  ",
            'content': 'this',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add title to your entry", 
            response.data
            )

    def test_for_error_returned_when_modifying_with_no_content_key(self):
        dummy_data = json.dumps({
            'id': '3', 
            'title': 'this',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add content and try again", 
            response.data
            )    
        
    def test_for_error_returned_when_modifying_with_no_content_value(self):
        dummy_data = json.dumps({
            'id': '3', 
            'title':"this",
            'content': '',
            'date': '5-6-8',
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"please add write something in the content", 
            response.data
            )            
    
    '''taste if modification is succesful'''
    def test_for_success__on_update(self):
        new_data = json.dumps({
            'id': '3',
            'title': 'new title', 
            'content': 'content stuff',
            'date': '5-6-8'
            })
        self.response
        self.tester.put(
            '/api/v1/entries/3',
            data=new_data,
            content_type='application/json'
            )
        response = self.tester.get('/api/v1/entries/3')
        self.assertEqual(response.status_code, 200) 
        
           
if __name__ == "__main__":
    unittest.main()