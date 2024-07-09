# super class
  '''there is a super class to access the method of parent class having same name here in below example
    it is 'home' '''

class Father:
    def home(self):
        print("1BHK")


class Son(Father):
    def home(self):
        super().home()
        print("3BHK")


sipu=Son()
sipu.home()


#o/p= 1BHK
#     3BHK

