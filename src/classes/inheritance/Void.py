from Cat import Cat

class Void(Cat):

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
        
    def hide_in_shadows(self):
        print("You are hiding in the shadows!")

roswell = Void("Roswell", 6, "black")
franklin = Cat("Franklin", 13)

roswell.hide_in_shadows()
franklin.hide_in_shadows()