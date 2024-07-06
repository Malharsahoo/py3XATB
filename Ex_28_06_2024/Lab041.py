# vwo login scenario with input() and constructor()

class VWOLoginScenario:

    def __init__(self,user_name_arg,password_arg):
        self.user_name=user_name_arg
        self.password=password_arg


    def login_page(self):
        if self.user_name=="smalhar96@gmail.com" and self.password=="123":
            print("you are allowed to login")
        else:
            print("you are not allowed")


user_name=input("enter the user id\n")
password=input("enter the password\n")
sipu=VWOLoginScenario(user_name,password)
sipu.login_page()

user_name=input("enter the user id\n")
password=input("enter the password\n")
malhar=VWOLoginScenario(user_name,password)
malhar.login_page()


#o/p= enter the user id
#     smalhar96@gmail.com
#     enter the password
#     123
#     you are allowed to login
#     enter the user id
#     smalhar96@gmail.com
#     enter the password
#     1234
#     you are not allowed