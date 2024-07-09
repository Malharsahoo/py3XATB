# Hierarchical inheritance

class Father:
    def BHK1(self):
        print("1BHK")
class sipu(Father):
    def BHK2(self):
        print("2BHK")
class kunja(Father):
    def no_house(self):
        print("i have no house for myself")
class bishnu(Father):
    def BHK3(self):
        print("3BHK")

property_obj_1=bishnu()
print(property_obj_1.BHK3())
print(property_obj_1.BHK1())

property_obj_2=kunja()
print(property_obj_2.no_house())
print(property_obj_2.BHK1())

#o/p=3BHK
#None
#1BHK
#None
#i have no house for myself
#None
#1BHK
#None
