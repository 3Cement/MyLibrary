#!/usr/bin/env python
import os, unittest, subprocess
from sqlalchemy import create_engine
from mylibrary_database import Base, Book, Category, Form

from flask import Flask
from flask_testing import TestCase
from mylibrary import create_app, db

class MyTest(TestCase):

	def create_app(self):
   		SQLALCHEMY_DATABASE_URI = "sqlite://"
    	TESTING = True
    	
    def create_app(self):

        # pass in test configuration
        return create_app(self)

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()