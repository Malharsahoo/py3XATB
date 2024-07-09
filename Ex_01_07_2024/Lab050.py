# hybrid inheritance

class A:
    def methodA(self):
        return "method A"
class B(A):
    def methodB(self):
        return "method B"
class C(A):
    def methodC(self):
        return "method C"
class D(B,C):
    def methodD(self):
        return "method D"


d=D()
print(d.methodB())
print(d.methodA())
print(d.methodD())
print(d.methodC())


#o/p=method B
#    method A
#    method D
#    method C
