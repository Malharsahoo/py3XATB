'''class VWOLoginPage:


    def login_confirm(self):
        if self.username=="smalhar96@gmail.com" and self.password==("123"):
            print("allowed to enter the class")
        else:
            print("you are not allowed")


sipu=VWOLoginPage()
sipu.username="smalhar96@gmail.com"
sipu.password="123"
sipu.login_confirm()

amit=VWOLoginPage()
amit.username="amit@gmail.com"
password="123"
amit.login_confirm() '''

#o/p= allowed to enter the class
#you are not allowed



#           --------with constructor--------
class VWOLoginPage:

    def __init__(self,user_name_arg,password_arg):
        self.username=user_name_arg
        self.password=password_arg

    def login_confirm(self):
        if self.username=="smalhar96@gmail.com" and self.password=="123":
            print("you are allowed to login")
        else:
            print("you are not allowed")

sipu=VWOLoginPage("smalhar96@gmail.com","123")
sipu.login_confirm()

malhar=VWOLoginPage("smalhar96@gmail.com","1234")
malhar.login_confirm()
#o/p= you are allowed to login
#you are not allowed
