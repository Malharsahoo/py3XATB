class VWOLogin_Scenario:

    def __init__(self,email,password,name):
        self.__email=email
        self.__password=password
        self.name=name

    def login_confirm(self):
        if self.__email=="abc789@gmail.com" and self.__password=="123":
            print("user is allowed")
        else:
            print("user is not allowed")

page1=VWOLogin_Scenario("abc789@gmail.com","123","malhar")
page1.login_confirm()
print(page1.name)

#o/p= user is allowed
#     malhar