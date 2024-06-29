# Decorators
'''Decorator is a function that takes another function as argument
and return a new function by extending it's behaviour'''

'''def decorator_function(func):
     def wrapper():
         print("hello")
         print("123")
         func()
         print("this is after decorator function")
         print("hope you get it")
     return wrapper()
@decorator_function
def another_functon_to_be_argument ():
    print("this is decorator function")'''
#O/p=hello
#123
#this is decorator function
#this is after decorator
#hope you get it




''' import time

def note_time_decorator(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print("Time_taken="+str(end_time-start_time))
    return wrapper()

@note_time_decorator
def logs_function():
    time.sleep(5)
    print("print the logs of time taken") '''

#o/p= print the logs of time taken
#     Time_taken=5.001377105712891

# benefit of using this is suppose in future we have another function, we can use it
#suppose we have an another function called reporting function()
'''  @note_time_decorator
     def reporting_function():
     time.sleep(2)
     print("print the reports of time taken")  '''

#print the logs of time taken
#Time_taken=5.000906229019165
#print the reports of time taken
#Time_taken=2.0015146732330322



# we can have multiple decorators also

''' def decorator1(func):
    def wraapper():
        print("decorator1")
        func()
    return wraapper
def decorator2(func):
    def wraapper():
        print("decorator2")
        func()
    return wraapper
@decorator2
def say_hello():
    print("this line is hello function for decorator function 2")
say_hello()
@decorator1
def say_hello():
    print("this line is hello function for decorator function 1")
say_hello() '''


#decorator2
#this line is hello function for decorator function 2
#decorator1
#this line is hello function for decorator function 1





'''import time
n=int(input("enter a no:\n"))

def my_timer_2(func):
    def wrapper():
        print("execute the function")
        func()
    return wrapper
def my_timer_1(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print("time taken to execute the function is: ", end_time-start_time)
    return wrapper
@my_timer_1
@my_timer_2
def squares():
    result=n**2
    print(f"the square of the number {n} is: {result}")
    time.sleep(3)
squares()'''


#o/p=enter a no:
#5
#execute the function
#the square of the number 5 is: 25
#time taken to execute the function is:  3.0005712509155273


import time
n=int(input("enter a no:\n"))
def my_timer_1(func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()
        print("time taken to execute the function is: ", end_time-start_time)
    return wrapper
def my_timer_2(func):
    def wrapper():
        dic=
        print("execute the function")
        func()
    return wrapper
@my_timer_2
@my_timer_1
def squares():
    result=n**2
    print(f"the square of the number {n} is: {result}")
    time.sleep(3)
squares()

