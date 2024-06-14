# script to find the square and qube of number 2
#              ------M1------
'''import math
num=2
square=num**2
qube=math.pow(num,3)
print("the square of the number is",square,"\nand the qube of the number is",qube)
print(type(square))
print(type(qube))'''
#Res= the square of the number is 4, and the qube of the number is 8.0, <class 'int'>, <class 'float'>

#               ------M2--------
import math
num=int(input("enter the value\n"))
print(f"the square of the number is:{num**2}",f"\nthe qube of the number is:{math.pow(num,3)}")
#Res= enter the value, 2    ,, the square of the number is:4, the qube of the number is:8.0

