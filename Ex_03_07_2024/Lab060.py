#          we can create our own exception also. this is called custom exception

class MycustomException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)


balance=100
withdraw_amount=int(input("enter the amount you want to withdraw\n"))
if withdraw_amount>balance:
    raise Exception(" your balance is low")
else:
  print("your remaining balance is",(balance-withdraw_amount))
