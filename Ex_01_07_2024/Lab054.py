from abc import ABC, abstractmethod
class Pyatb(ABC):
    def payfee(self):
        pass

    def enrolled(self):
        print("enrolled")

class Sipu(Pyatb):
    def payfee(self):
        print("paid")

kunja=Sipu()
kunja.payfee()
kunja.enrolled()

#o/p=   paid
#       enrolled
