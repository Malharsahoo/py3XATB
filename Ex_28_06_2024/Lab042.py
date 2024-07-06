'''private data like private variables and private functions can only
be accessible through a method which is only within the class'''

class Myclass:
    def __init__(self):
        self.__name="sipu"                  #private variable
        self.__email="smalhar96@gmail.com"  #private variable  denoted as .__
    def public_function(self):
        print("it is public()")
    def __private_function(self):      # this is a private method/function
        print("your mail id is-",self.__email)
        print("this is a private function, you can only access this via another method")
    def public_functon_for_private_method(self):
        self.__private_function()
        print(self.__name)

sipu=Myclass()
sipu.public_functon_for_private_method()

#    o/p=your mail id is- smalhar96@gmail.com
#    this is a private function, you can only access this via another method
#    sipu

'''here in above, public method of line 13 which is inside the class has access data of
 private function of line 10 and private instance variable of line 6.. we can
  access all those outside of the class while creating object by calling the public
  method of class which is line no 13'''