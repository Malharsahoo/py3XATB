# geter setter in python

class Password_edit:
    def __init__(self,pwd):
        self.__password=pwd
        self.public_var=10

    def get_pswd(self,is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("invalid password")

    def set_pswd(self,pwd):
        if len(pwd)>10:
            if pwd.endswith("9"):
               self.__password=pwd
               print("set to correct", self.__password)
            else:
               print("not allowed, check password end digit")
        else:
           print("not allowed, invalid password length")


ref_obj_for_password=Password_edit("hacker123")
ref_obj_for_password.get_pswd(True)
ref_obj_for_password.set_pswd("malharsahoo79")


#o/p= hacker123
#     set to correct malharsahoo79
