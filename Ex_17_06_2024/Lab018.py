#User Defined functions

#no return type, no paramters

#def say_hello():
#    print("hello")
#res=say_hello()
#print(res)


'''o/p= hello
   none'''


# no return type with arguments
#def say_hello_argumets(name):
#    print("hello", name)
#say_hello_argumets("sipu")
#say_hello_argumets("kunja")


'''O/P-hello sipu
hello kunja'''

#res=say_hello_argumets("bishnu")
#print(res)

'''O/P-hello bishnu
None'''




#no return type with default argument
#def say_hello_arg_default(name="sipu"):
#    print("hello",name)
#say_hello_arg_default()
#say_hello_arg_default("bishnu")
#res=say_hello_arg_default(name="kunja")
#print(res)
'''O/P- hello sipu
hello bishnu
hello kunja
None
'''




# with arguments with return

#def sum_number_argument_with_return(a,b):
#    return a+b
#res=sum_number_argument_with_return(12,15)
#print(res)
'''O/P= 27'''


#we can also pass the argument values when we know about the arguments in definition

def sum_number_argument_with_return(a,b):
    return a+b
res=sum_number_argument_with_return(a=44,b=33)
print(res)
'''O/P=77'''