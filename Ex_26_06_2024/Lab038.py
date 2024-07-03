'''class calculator:
    def sum(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def divi(self,a,b):
        return a/b

object_reference=calculator()
sum_of_func=object_reference.sum(3,4)
sub_of_func=object_reference.sub(7,9)
divi_of_func=object_reference.divi(7,4)
print(sub_of_func)
print(sum_of_func)
print(divi_of_func)   '''

# O/p= -2
#       7
#     1.75


''' ideally generally people dont create constructor, rarely they create a constructor if 
    they want to run a special method while creating an object  '''

# with cnstructor
class calc:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mult(self):
        return self.a*self.b

    def divi(self):
        return self.a/self.b


print(calc(12,15).sum())
obj_ref=calc(12,17)
output=obj_ref.sum()
print(output)


#o/p= 27
#  29