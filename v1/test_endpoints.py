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
    '''testing if database is empty'''
    def test_for_error_returned_when_no_entries(self):
        response = self.tester.get('/api/v1/entries')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"no entries added, please add an entry", response.data)

    '''testing the get with the data'''
    def test_success_for_get_all_entries(self):
        self.tester.post(
        '/api/v1/entries',
        data=self.data,
        content_type='application/json'
        )
        response = self.tester.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)

    '''testing for invalid keys passed'''
    def test_for_error_returned_when_invalid_keys(self):
        dummy_data = json.dumps({
            'id': '3',
            'tit': 'this', 
            'body': 'this content',
            'date': '5-6-8'
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=dummy_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 403)
        self.assertIn(
            b"key should be id ,content ,date and title", 
            response.data
            )    
    '''testing if the value entered is empty'''
    def test_for_error_returned_when_empty_values(self):
        test_data = json.dumps({
            'id': '3',
            'title': '', 
            'content': '',
            'date': '5-6-8'
            })
        response = self.tester.post(
            '/api/v1/entries', 
            data=test_data,
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 403)
        self.assertIn(b"one or more of your key values are empty. please check and try again", response.data)

    '''testing if specified entry is not in the database'''
    def test_for_error_for_no_specified_entry(self):
        response = self.tester.get('/api/v1/entries/id')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"no entries added, please add an entry", response.data)

    '''#testing wether a specific is succesfully fetched'''
    def test_for_sucessfull_get_specific_entry(self):
        self.tester.post(
            '/api/v1/entries',
            data=self.data,
            content_type='application/json'
            )
        response = self.tester.get('/api/v1/entries/3')
        self.assertEqual(response.status_code, 200)       
    '''taste if pu method is succesful'''
    def test_for_success__on_update(self):
        new_data = json.dumps({
            'id': '3',
            'title': 'new title', 
            'content': 'content stuff',
            'date': '5-6-8'
            })
        self.tester.post(
            '/api/v1/entries',
            data=self.data,
            content_type='application/json'
            )
        self.tester.put(
            '/api/v1/entries/3',
            data=new_data,
            content_type='application/json'
            )
        response = self.tester.get('/api/v1/entries/3')
        self.assertEqual(response.status_code, 200)    
if __name__ == "__main__":
    unittest.main()