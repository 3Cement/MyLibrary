import os, sys

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()

#Making an API Endpoint (GET Request)

class Category(Base):
	__tablename__ = 'Category'
	name = db.Column(String(80), nullable = False)
	id = db.Column(Integer, primary_key = True)
	#books = relationship('Book', backref='category', lazy=True)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

association_table = Table('association', Base.metadata,
	db.Column('book_id', Integer, ForeignKey('Book.id')),
	db.Column('form_id', Integer, ForeignKey('Form.id'))
	)

class Book(Base):
	__tablename__ = 'Book'
	name = db.Column(String(80), nullable = False, unique=True)
	id = db.Column(Integer, primary_key = True)
	author = db.Column(String(30))
	language = db.Column(String(30))
	category_id = db.Column(Integer, ForeignKey('Category.id'), nullable = False)
	category = db.relationship('Category')
	forms = db.relationship("Form", secondary=association_table, back_populates="books")

	def __repr__(self):
		return '<Book %r>' % self.name

class Form(Base):
	__tablename__ = 'Form'
	name = db.Column(String, nullable = False)
	id = db.Column(Integer, primary_key=True)
	books = db.relationship("Book", secondary=association_table, back_populates="forms")

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

### insert at end of file ###
engine = create_engine('sqlite:///allbooks.db')
Base.metadata.create_all(engine)