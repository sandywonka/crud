class Parent(object):
    def __init__(self, name):
        self._name = name
        raise NotImplementedError("Please override!")

    def show(self):
        print(self._name)


class Child(Parent):
    def __init__(self, name):
        self.name = name

    def show_parent(self, name):
        self.__name = name

    def show(self, name):
        self._name = name

    @property
    def value(self):
        return self._name

    @value.setter
    def value(self, name):
        self._name = name


kapal = Child("Kapal Pesiar")
kapal.show_parent("Perahu Motor")
kapal.show("Kapal Layar")
print(kapal.__dict__)
kapal.value = "Kapal Selam"
print(kapal.value)
