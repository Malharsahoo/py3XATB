                   #                  Exception handling
'''exception is an event that occurs during the execution of a program and disrupt the normal flow
   of instructions'''
'''exception handling is done to improve user experience'''


try:
    a= int(input("enter the value of num1 \n"))
    b= int(input("enter the value of num2 \n"))
    c=a/b
    print("result of division is", c)
except Exception as e:
    print(e)
    print("please enter integer value only")

'''in above example if we enter any chracter or string value instead of integer then the error message
   in execution will displayed as 'invalid literal for int() with base 10: "spu' ' which is not red color
    as we have print it as print(e) and along with this, a message is also displayed as 'please enter integer
    value only' which generally enhance user experience '''