# sandbox environment for testing purposes

from Book import Book
from Owner import Owner

jungle = Book("The Jungle", "Upton Sinclair")
gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")
quixote = Book("Don Quixote", "Miguel de Cevantes Savedra")

clarice = Owner("Clarice")
mustard = Owner("Coronel Mustard")
x = 3 #will throw an error because its not an instance of the Owner class

jungle.owner = clarice
clarice.books = jungle

gatsby.owner = clarice
clarice.books = gatsby
quixote.owner = mustard
mustard.books = quixote

print(jungle.owner)
print(clarice.books[0])

for book in clarice.books:
    print(book)

quixote.turn_the_page()

print(mustard.books[0])
print(mustard.books[0].turn_the_page())