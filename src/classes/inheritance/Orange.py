from Cat import Cat

class Orange(Cat):

    def __init__(self, name, age, color):
        self._color = color
        super().__init__(name, age)

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if type(color) == str:
            self._color = color
        else:
            raise Exception
    
    def meow(self):
        print("I am an orange cat!")
        
timmy = Orange("Timmy", 4, "orange")

print(timmy)