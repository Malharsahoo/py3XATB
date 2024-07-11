# we also have else.. when the code is free from any error then else part will be executed

try:
    num1=int(input("enter the value of number 1 \n"))
    num2=int(input("enter the value of number 2 \n"))
    result=num1/num2
except ValueError as ve:
    print(ve)

except ZeroDivisionError as zde:
    print(zde)

else:
    print(f"the result of division is {result}")

finally:
    print("I will be executed anyhow")

# enter the value of number 1
# 50
# enter the value of number 2
# 25
# the result of division is 2.0
# I will be executed anyhow


# enter the value of number 1
# 25
# enter the value of number 2
# sipu
# invalid literal for int() with base 10: 'sipu'
# I will be executed anyhow


# enter the value of number 1
# 27
# enter the value of number 2
# 0
# division by zero
# I will be executed anyhow

''' here in above since line 4,5,6 doesn't have any error so the line number 13(else) executed
    if there is any issue in line 3,4 then line no 13 will not be executed, line 7 will executed
    if there is any issue in line number 6 the line 10 will be executed, line 13 will not be executed
    irrespective of any errors line number 16(finally) will always execute..'''