# polymorphism
'''polymorphism means a term used to refer to an object's ability to take on multiple forms
   an object let's say sipu can be a mentor,husband,brother for different different classes'''

# method overriding polymorphism
''' it means same name in parent and child class. child always override the parent function'''

#class Father:
#    def home(self):
#        print("1BHK")
#class Son:
#    def home(self):
#        print("3BHK")

#obj1=Son()
#print(obj1.home())

#o/p= 3BHK

'''here in above both father and son class have same method named 'home'. child class that is 
 son class home method is overriden to different role '''

class Shape:
    def area(self):
        print("area of the shape")
class rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

obj1=rectangle(3,4)
print(obj1.area())                #o/p=12

obj2=circle(10)
print(obj2.area())                #o/p=314.0


'''here in above parent class is shape.. and it has two child class named rectamgle and 
   circle. both of three have same method named area. here in above method area of parent
   class is overriden to different different role for child class. so object is behaving
   differently for different class here'''