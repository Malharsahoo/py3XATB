#             --------------  constructors-----------

#parameter constructors
class dog:
    name=None
    id=None

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def sleep(self):
      print("who is sleeping------>"+self.name)



dog1=dog("chow","1")
dog2=dog("meow","2")
print(f"{dog1.name} has id no {dog1.id}")
print(f"{dog2.name} has id no {dog2.id}")
dog2.sleep()


#o/p= chow has id no 1
#     meow has id no 2
#     who is sleeping------>meow