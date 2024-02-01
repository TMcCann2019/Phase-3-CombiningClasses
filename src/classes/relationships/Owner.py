class Owner():

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # if not hasattr(self, "name"):
        self._name = name
        # else:
        #     raise Exception("Owner cannot be given a new name!")

# o = Owner("Bob")

# # o.name = "Sandy" #cannot do this line if hasattr. Will raise the exception. if no hasattr you can reset the name

# print(o.name)