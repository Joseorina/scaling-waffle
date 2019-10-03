import unittest
import os 
import json
from app import create_app, db

class BucketListTestCase(unittest.TestCase):
    """
    Class representing the bucketlist testcase
    
    Arguments:
        unittest {[type]} -- [description]
    """

    def setUp(self):
        """
        Initialize app and test variables
        """
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.bucketlist = {'name': 'Go to dubai for vacay'}

        """
        Bind app to current context
        """

        with self.app.app_context():
            """
            Create all tables
            """
            db.create_all()
    
    def test_bucketlist_creation(self):
        """
        test if API endpoint can create an item(POST)
        """
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Go to dubai', str(res.data))
    def test_api_get_all(self):
        pass

    def test_api_get_single_item(self):
        pass

    def test_edit_item(self):
        pass

    def test_delete_items(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

    