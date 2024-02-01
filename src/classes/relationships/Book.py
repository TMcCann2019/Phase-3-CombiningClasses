class Book:

    def __init__(self, title, author):
        self._title = title
        self._author = author

        self._owner = None

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if type(title) == str:
            self._title = title
        else:
            raise Exception("The title must be a string!")
        
    def get_author(self):
        return self._author
    
    def set_author(self, author):
        if type(author) == str and len(author) > 4:
            self._author = author
        else:
            raise Exception("The author must be a string of greater than 4 characters!")
        
    author = property(get_author, set_author)

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        from Owner import Owner
        if isinstance(owner, Owner):
            self._owner = owner
        else:
            raise Exception("The owner must be an instance of the Owner class!")
        
    def turn_the_page(self):
        print(f"Turning to the next page for {self.title}")
        
    def __str__(self):
        return f"Book: {self.title} by {self.author}"