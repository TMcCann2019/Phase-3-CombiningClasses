class Owner():

    def __init__(self, name):
        self.name = name
        self._books = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # if not hasattr(self, "name"):
        self._name = name
        # else:
        #     raise Exception("Owner cannot be given a new name!")

    @property
    def books(self):
        return self._books
    
    @books.setter
    def books(self, books):
        from Book import Book
        if isinstance(books, Book) and books not in self._books:
            self._books.append(books)
        else:
            raise Exception("The book must be an instance of the Book class and be new to me!")

    def __str__(self):
        return f"Owner: {self.name}"
        

# o = Owner("Bob")

# # o.name = "Sandy" #cannot do this line if hasattr. Will raise the exception. if no hasattr you can reset the name

# print(o.name)