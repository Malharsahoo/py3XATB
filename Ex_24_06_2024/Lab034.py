#Recursion concept
'''it is a programming technique where a function call itself to solve a problem
   here it has 2 key concepts(base case,recursive case)
      first recursive case will run until we reach to base case'''

'''def factorial(n):
    # base case
    if n==0 or n==1:
        return 1
    # recursive case
    else:
        return n*factorial(n-1)
fact=factorial(5)
print(fact)'''
#o/p=120




#sum of digits of a number
def sum_of_digits(num):
    #Base Case
    if num<10:
        return num
    #Recursive case    
    else:
        return num % 10 + sum_of_digits(num//10)
print(sum_of_digits(12345))
#o/p=15


#    Or       ----------M2------------
def sum_of_digits(num):
    sum_digits=0
    while num>0:
        sum_digits=sum_digits+num%10
        num=num//10
    return sum_digits
print(sum_of_digits(12345))
