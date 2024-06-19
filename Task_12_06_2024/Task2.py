# Trangle Classifier
side1=int(input("enter the value of side1\n"))
side2=int(input("enter the value of side2\n"))
side3=int(input("enter the value of side3\n"))
if side1==side2 and side1==side3:
    print("the triangle is Equilateral triangle")
elif side1==side2 or side1==side3 or side2==side3:
    print("the triangle is Isosceles")
elif side1!=side2 and side1!=side3 and side2!=side3:
    print("the triangle is scalene")
else:
    print("invalid triangle")