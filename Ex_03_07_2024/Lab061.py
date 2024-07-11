                             # main function in python


''' def this_is_my_main_fn():
    print(" main called")

 
if __name__=="__main__":
    this_is_my_main_fn() '''

# o/p= main called



   #  python allow us to have multiple main functions()

def f1():
    print("function1")

def f2():
    print("function2")


def f3():
    print("function3")



def main():
    print("main")

if __name__=="__main__":
    f2()
    main()
    f1()


# op= function2
#     main
#     function1