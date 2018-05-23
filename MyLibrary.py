#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from flask import Flask, render_template, request, redirect, url_for, flash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from mylibrary_database import Base, Book, Category, Form, db

#db = SQLAlchemy()
def create_app():
	app = Flask(__name__)
	db.init_app(app)

	engine = create_engine('sqlite:///allbooks.db', connect_args={'check_same_thread': False})
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()

	@app.route('/')
	@app.route('/books/')
	def showBooks():
		#book = session.query(Book)
		books = session.query(Book).all()
		categories = session.query(Category).all()
		if not books:
			flash("Your Library is Empty")
		return render_template('books.html', books=books, categories=categories)

	languages = ['Polish', 'English']

	@app.route('/books/new/', methods=['GET', 'POST'])
	def newBook():
		categories = session.query(Category).all()
		forms = session.query(Form).all()
		#languages = session.query(Languages).all()
		if request.method == 'POST':
			newBook = Book(name = request.form['name'], 
							author = request.form['author'], 
							category = session.query(Category).filter_by(name=request.form.get('category')).one(),
							forms = [Form(name) for name in request.form.getlist('form')], 
							#works, I get both elements in the list, but I create new Form object
							#forms = [session.query(Form).filter_by(name=request.form.get('form')).one()], 
							#works, I do not create new Form object, but I get only one element in the list.
							language = request.form['language'])
			session.add(newBook)
			session.commit()
			flash(newBook.name+'book, in category '+newBook.category.name+' added!')
			return redirect(url_for('showBooks'))
		else:
			return render_template('newBook.html', languages=languages, categories=categories, forms=forms)

	@app.route('/books/<int:book_id>/edit/', methods=['GET','POST'])
	def editBook(book_id):
		bookToEdit = session.query(Book).filter_by(id=book_id).one()
		if request.method == 'POST':
			if request.form['name']:
				bookToEdit.name = request.form['name']
				bookToEdit.author = request.form['author']
				bookToEdit.category = request.form['category']
				bookToEdit.language = request.form['language']
			session.add(bookToEdit)
			session.commit()
			flash("Book has been edited")
			return redirect(url_for('showBooks'))
		else:
			return render_template('editBook.html', book_id=book_id, book=bookToEdit, languages=languages)

	@app.route('/books/<int:book_id>/delete/', methods=['GET','POST'])
	def deleteBook(book_id):
		bookToDelete = session.query(Book).filter_by(id=book_id).one()
		if request.method == 'POST':
			session.delete(bookToDelete)
			session.commit()
			flash("Book has been deleted")
			return redirect(url_for('showBooks'))
		else:
			return render_template('deleteBook.html', book_id=book_id, book=bookToDelete)

	if __name__ == '__main__':
		app.secret_key = 'super_secret_key'
		app.debug = True
		app.run(host='0.0.0.0', port=5000)

	return app

create_app()


# USER - SING IN LOG IN etc.
# NEW LIBRARY for USER
# LANDING PAGE
# Categories - SPORT, BIZNESS, ROZRYWKA
# FORM - BOOK, EBOOK, AUDIOBOOK etc.
# Language - PL, ENG