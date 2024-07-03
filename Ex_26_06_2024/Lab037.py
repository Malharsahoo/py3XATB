# default constructors
class dog:
    name=None
    id=None
    def __init__(self,name="sipu",id="7"):
        self.name=name
        self.id=id

    def sleep(self):
      print("who is sleeping------>"+self.name)



dog1=dog("chow","1")
dog2=dog("meow","2")
dog3=dog()
print(f"{dog1.name} has id no {dog1.id}")
print(f"{dog2.name} has id no {dog2.id}")
print(f"{dog3.name} has id no {dog3.id}")
dog1.sleep()
dog2.sleep()
dog3.sleep()


#chow has id no 1
#meow has id no 2
#sipu has id no 7
who is sleeping------>chow
who is sleeping------>meow
who is sleeping------>sipu