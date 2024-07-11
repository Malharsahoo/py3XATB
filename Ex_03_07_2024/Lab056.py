                          # try, except, finally

try:
    num1=int(input("enter the value of number 1 \n"))
    num2=int(input("enter the value of number 2 \n"))
    result=num1/num2
    print(result)
except ValueError as ve:
    print(ve)

except ZeroDivisionError as zde:       # we can have multiple exception as well
    print(zde)

finally:
    print("I will be executed anyhow")


'''    enter the value of number 2 
sipu
invalid literal for int() with base 10: 'sipu'
I will be executed anyhow
'''

''' finally means anyhow the code will be executed'''