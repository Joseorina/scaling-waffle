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
		#check 201 status(created)
		self.assertEqual(res.status_code, 201)
		self.assertIn('Go to dubai', str(res.data))


	def test_api_get_all(self):
		"""
		test if API can ge a bucket list(GET)
		"""
		res = self.client().post('/bucketlists/', data=self.bucketlist)
		self.assertEqual(res.status_code, 201)
		res = self.client().get('/bucketlists/')
		self.assertEqual(res.status_code, 200)
		self.assertIn('Go to dubai', str(res.data))

	def test_api_get_single_item(self):
		"""
		test if API can get a single bucketlist
		"""
		rv = self.client().post('/bucketlists/', data=self.bucketlist)
		self.assertEqual(rv.status_code, 201)
		result_in_json = json.loads(rv.data.decode('utf-8').replace("'","\""))
		result = self.client().get(('/bucketlists/{}'.format(result_in_json['id'])))
		self.assertEqual(result.status_code, 200)
		self.assertIn('Go to dubai', str(result.data))

	def test_edit_item(self):
		"""
		Test if API can edit existing items
		"""
		rv = self.client().post(
			'/bukcetlists/',
			data = {
				'name':'Eat, pray and love'})
		self.assertEqual(rv.status_code, 201)
		rv = self.client().put(
			'/bucketlists/1',
			data = {
				"name": "Dont just eat but also pray and love :-"})
		self.assertEqual(rv.status_code, 200)
		results = self.client().get('/bucketlists/1')
		self.assertIn('Dont just eat')		

	def test_delete_items(self):
		"""
		Test if API can delete an item(DELETE request)
		"""
		rv = self.client().post(
			'buckelists/1',
			data = {'name':'Eat, pray and love'})
		self.assertEqual(rv.status_code, 201)
		res = self.client().delete('/bucketlists/1')
		self.assertEqual(res.status_code, 200)
		result = self.client().delete('/bucketlists/1')
		self.assertEqual(result.status_code, 404)	

	def tearDown(self):
		"""
		Tear down all initialized variables
		"""
		with self.app.app_context():
			#Drop all tables
			db.session.remove()
			db.drop_all()


if __name__ == "__main__":
	unittest.main()
