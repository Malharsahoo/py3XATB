# input() with constructor
class student:
    def __init__(self):
        self.name=input("enter your name")
        self.age=int(input("enter your age"))

    def display(self):
        print(f"your name is {self.name} and your age is {self.age}")

display=student()
display.display()

#o/p= enter your namesipu
#enter your age55
#your name is sipu and your age is 55
