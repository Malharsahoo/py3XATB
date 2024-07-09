                              # ABSTRACTION


class Animal(ABC):
        def __init__(self,name):
            self.name=name
        def sound(self):
            pass

class Dog(Animal):
     def sound(self):
       return "Bark"        #  definition of sound is given

class Cat(Animal):
    def sound(self):
        return "meow"        #  definition of sound is given

dog=Dog("sipu")
print(dog.sound())

#o/p=Bark
'''abstract method is used to force something here in above incomplete sound method in parent class lets say
animal class is forced to defined in other classes like dog and cat'''