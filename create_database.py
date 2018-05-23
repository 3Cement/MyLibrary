from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mylibrary import db
from mylibrary_database import Base, Book, Category, Form

engine = create_engine('sqlite:///allbooks.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# ADD BOOKS TO DATABASE

paperback = Form(name="Paperback")
ebook = Form(name="Ebook")
audiobook = Form(name="Audiobook")
session.add(paperback)
session.add(ebook)
session.add(audiobook)
session.commit()
print('3 forms added')

# TUTAJ ZROBIC WSZEDZSIE TRY: EXCEPT, INTEGRITYERROR itp.

sport = Category(name='Sport')
rozrywka = Category(name='Rozrywka')
finanse = Category(name='Finanse')
rozwoj_osobisty = Category(name='Rozwoj Osobisty')
odzywianie = Category(name='Odzywianie')
session.add(sport)
session.add(rozrywka)
session.add(finanse)
session.add(rozwoj_osobisty)
session.add(odzywianie)
session.commit()
print('5 categories added!')

ks1 = Book(name="Ksiazka1", author="Author1", category=finanse, forms=[paperback], language="Polish")
ks2 = Book(name="Ksiazka2", author="Author2", category=odzywianie, forms=[ebook, audiobook], language="English")
ks3 = Book(name="Ksiazka3", author="Author3", category=rozrywka, forms=[audiobook, ebook], language="Polish")
ks4 = Book(name="Ksiazka4", author="Author4", category=sport, forms=[audiobook, paperback], language="English")
ks5 = Book(name="Ksiazka5", author="Author5", category=rozwoj_osobisty, forms=[paperback], language="Polish")
ks6 = Book(name="Ksiazka6", author="Author6", category=finanse, forms=[ebook, paperback], language="English")
ks7 = Book(name="Ksiazka7", author="Author7", category=finanse, forms=[audiobook], language="English")
ks8 = Book(name="Ksiazka8", author="Author8", category=sport, forms=[paperback], language="Polish")
ks9 = Book(name="Ksiazka9", author="Author9", category=rozwoj_osobisty, forms=[ebook], language="Polish")
session.add(ks1)
session.add(ks2)
session.add(ks3)
session.add(ks4)
session.add(ks5)
session.add(ks6)
session.add(ks7)
session.add(ks8)
session.add(ks9)
session.commit()
print('9 books added!')
'''
book1 = Book(name="Ksiazka1", author="Author1", category="KATEGORIA1", nbook="Book", language="Polish")
book2 = Book(name="Ksiazka2", author="Author2", category="KATEGORIA2", ebook="Ebook", language="English")
book3 = Book(name="Ksiazka3", author="Author3", category="KATEGORIA3", audio="Audiobook", language="Polish")
book4 = Book(name="Ksiazka4", author="Author4", category="KATEGORIA4", 
			nbook="Book", ebook="Ebook", audio="Audiobook", language="English")
book5 = Book(name="Ksiazka5", author="Author5", category="KATEGORIA1", nbook="Book", ebook="Ebook", language="Polish")
book6 = Book(name="Ksiazka6", author="Author6", category="KATEGORIA2", ebook="Ebook", audio="Audiobook", language="English")
book7 = Book(name="Ksiazka7", author="Author7", category="KATEGORIA3", audio="Audiobook", language="Polish")
book8 = Book(name="Ksiazka8", author="Author8", category="KATEGORIA1", nbook="Book", language="Polish")
book9 = Book(name="Ksiazka9", author="Author9", category="KATEGORIA2", ebook="Ebook", language="English")
book10 = Book(name="Ksiazka10", author="Author10", category="KATEGORIA3", audio="Audiobook", language="Polish")
book11 = Book(name="Ksiazka11", author="Author11", category="KATEGORIA4", 
			nbook="Book", ebook="Ebook", audio="Audiobook", language="English")
book12 = Book(name="Ksiazka12", author="Author12", category="KATEGORIA1", nbook="Book", ebook="Ebook", language="Polish")
book13 = Book(name="Ksiazka13", author="Author13", category="KATEGORIA2", ebook="Ebook", audio="Audiobook", language="English")
book14 = Book(name="Ksiazka14", author="Author14", category="KATEGORIA3", audio="Audiobook", language="Polish")

session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(book5)
session.add(book6)
session.add(book7)
session.add(book8)
session.add(book9)
session.add(book10)
session.add(book11)
session.add(book12)
session.add(book13)
session.add(book14)
session.commit()

print("14 books added!")
'''