# multiple inheritance
class Father:
    def father_money(self):
        return "5"
    def home(self):
        return "this home is frome the father"
class Mother:
    def mother_money(self):
        return "3"
    def home(self):
        return "this home is mother's home"
#class Son(Mother,Father):
#    def son_money(self):
#        return "1"
#    def home(self):
#        return "this is son home"

#child=Son()
#print(child.son_money())
#print(child.father_money())
#print(child.mother_money())
#print(child.home())

#o/p=1
#    5
#    3
#    this is son home
'''since home method is common across three classes, so preference will be given
to the local classes to execute the common method to execute'''


''' lets say if son class doesnt have any home method, then preference will  be given
to the class order to inherit first'''

#class Son(Mother,Father):
#    pass

#child=Son()
#print(child.home())

#o/p= this home is mother's home


class Son(Father,Mother):
    pass

child=Son()
print(child.home())

#o/p=this home is frome the father
