#!/usr/bin/env python
import os, unittest, subprocess
from sqlalchemy import create_engine
from mylibrary import create_app, db
from mylibrary_database import Base, Book, Category, Form

class UserModelCase(unittest.TestCase):
    def setUp(self):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = 'sqlite://'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app_client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_forms(self):
        paperback = Form(name="Paperback")
        ebook = Form(name="Ebook")
        audiobook = Form(name="Audiobook")
        db.session.add(paperback)
        db.session.add(ebook)
        db.session.add(audiobook)
        db.session.commit()
        print('All 3 forms added!')
'''
    def test_categories(self):

    def test_books(self):

    def test_new_book(self):

    def test_main_page(self):
        response = self.app_client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
'''
if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
TEST_DB = 'test.db'
app = create_app()
app.app_context().push()

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        pass
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()

'''