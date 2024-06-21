'''def my_function():
    a=10
    print("hello")
print(a)
my_function()'''


'''a=10
def my_function():
    print("hello")
print(a)
my_function()'''


a=55
def outer_function():
    b=33
    def inner_function():
        print(b)
    inner_function()
print(a)
outer_function()



