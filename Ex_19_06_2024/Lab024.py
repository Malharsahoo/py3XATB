# lambda expression or one liners code execution

#def double_my_salary(salary):
#    return salary*2
#new_sal=double_my_salary(100)
#print(new_sal)
#o/p=200


'''instead of all we can simply execute single line of return code salary*2  by using
lambda expression while removing function name and just passing argument value..
or simply we can say lambda expression is used to convert our function to one liners'''

#by using lambda expression
#fun_double_my_sal= lambda salary: salary*2
#print(fun_double_my_sal(100))
#op=200




#sum of two numbers
#sum_of_two_no= lambda a,b:a+b
#print(sum_of_two_no(a=5,b=6))
#o/p=11



# odd even number checking
#def check_odd_even(num):
#    if num%2==0:
#       print(f"{num} is even")
#    else:
#        print(f"{num} is odd")
#check_odd_even((4))


#even_odd= lambda number: (f"{number} is even") if number%2==0 else (f"{number} is odd")
#print(even_odd(5))
#op= 5 is odd



#power of function using input function

power_of= lambda: int(input("Enter a number\n"))**2
res=power_of()
print(res)