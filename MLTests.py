#!/usr/bin/env python
import os, unittest 
from sqlalchemy import create_engine
from mylibrary import app, create_app, db
from mylibrary_database import Base, Book, Category, Form
'''
class TestConfig():
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite://'

class TestCase(unittest.TestCase):
	def setUp(self):
		#self.app = create_engine(TestConfig)
		self.app = app.test_client()

	def tearDown(self):
		session.remove()
		drop_all()
		self.app_context.pop()

	def test_main_page(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()

'''
	def setUp(self):
		self.app = create_engine(TestConfig)
		self.app_context = self.app.app_context()
		self.app_context.push()
		create_all()
		#Base.metadata.create_all(engine)
'''

#engine = create_engine('sqlite:///allbooks.db')
#Base.metadata.create_all(engine)