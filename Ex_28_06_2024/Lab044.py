# show balance and withdraw function with encapsulation
class BankAccount:
    def __init__(self):
        self.__balance=0
        self.__private_var=500
    def public_function(self):
        print(self.__private_var)

    def deposit(self,amount):
        self.__balance+=amount

    def __withdraw(self,amount):
         self.__balance-=amount

    def __show_balance(self):
         print("your balance is",self.__balance)

    def if_authozized_customer_to_show_balance(self,is_auth):
         if is_auth:
             self.__show_balance()
         else:
            print("you are not authorized to see balance")

    def if_you_are_authorized_to_withdraw(self,is_auth,amount):
         if is_auth:
            self.__withdraw(amount)
         else:
             print("you are not an authozied customer to withdraw money")


jp_chase=BankAccount()
jp_chase.deposit(400)
secret_password=input("enter your atm PIN to see the balance \n")
if secret_password == "123456":
    jp_chase.if_authozized_customer_to_show_balance(True)
else:
    jp_chase.if_authozized_customer_to_show_balance(False)

secret_password=input("enter your atm PIN to withdraw money \n")
if secret_password=="123456":
    withdraw_amount = int(input("enter the amount you want to withdraw \n"))
    jp_chase.if_you_are_authorized_to_withdraw(True,amount=withdraw_amount)
    jp_chase.if_authozized_customer_to_show_balance(True)
else:
    jp_chase.if_you_are_authorized_to_withdraw(False)


# O/P= enter your atm PIN to see the balance
#      123456
#      your balance is 400
#      enter your atm PIN to withdraw money
#      123456
#      enter the amount you want to withdraw
#      120
#      your balance is 280



