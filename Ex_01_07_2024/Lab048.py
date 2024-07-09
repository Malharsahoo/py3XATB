# multilevel inheritance

class Grandparent:
    gold_key="2kg"
    def grandparent_method(self):
        return "this is grand parent method"

class Parent(Grandparent):
    def parent_method(self):
        return "this is parent method"

class child(Parent):
    car="BMW"
    def child_method(self):
        return "this is child method"

ref_obj1=child()
print(ref_obj1.child_method())
print(ref_obj1.grandparent_method())
print(ref_obj1.parent_method())
print(ref_obj1.gold_key)
print(ref_obj1.car)

ref_obj2=Parent()
print(ref_obj2.gold_key)
print(ref_obj2.parent_method())
print(ref_obj2.grandparent_method())


ref_obj3=Grandparent()
print(ref_obj3.grandparent_method())
print(ref_obj3.gold_key)


#o/p=this is child method
#    this is grand parent method
#    this is parent method
#    2kg
#    BMW
#    2kg
#    this is parent method
#    this is grand parent method
#    this is grand parent method
#    2kg