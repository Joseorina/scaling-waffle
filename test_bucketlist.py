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

    def test_bucketlist_creation(self):
        """
        Create all tables
        """
        db.create_all()

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

    