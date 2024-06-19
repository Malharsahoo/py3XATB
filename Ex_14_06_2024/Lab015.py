#    Match case #Match case real time example will be executed in API Automation

'''name=input("enter your name\n")
match name:
    case "sipu":
        print("hello sipu","\nwelcome to the game zone")
    case "megha":
        print(" hi megha, how are you?")
    case "madan":
        print("your name is madan")
    case "akash":
        print("hello akash your subscription has ended. please recharge for entry")
        print("you can avail discount coupon offers over here")
    case _:
        print("invalid input. please recheck your name")'''

#                         -----------M3---------
'''num=int(input("enter a number\n"))
match num:
    case 1:
      print("you have entered 1")
      print("entered the second line also")
    case 2:
        print("you have entered 2")
    case 3:
        print("you have entered 3")
    case _:
        print("re check the numbers")'''



#                  _____________M3_____________
#  (a)
'''browser = "firefox"
match browser:
    case "chrome":
        print("execute the code for chrome browser")
    case "firefox":
        print("execute the code for firefox browser")
    case _:
        print(" no idea which browser")'''
#o/p= execute the code for firefox browser

#  (b)
'''browser = "edge"
match browser:
    case "chrome":
        print("execute the code for chrome browser")
    case "firefox":
        print("execute the code for firefox browser")
    case _:
        print(" no idea which browser")'''
#o/p= no idea which browser


#  (c)
browser=input("enter the browser name\n")
browser=browser.lower()
match browser:
    case "chrome":
        print("execute the code for chrome browser")
    case "firefox":
       num=int(input("enter a number\n"))
       if num%2==0:
           print("the number is even")
       else:
           print("the number is not even")
    case "edge":
        year=int(input("enter the value of a number\n"))
        if year%4==0 and year%400==0 or year%100!=0:
            print("the year is leap year")
        else:
            print("the year is not leap year")
    case _:
        print(" no idea which browser")



'''o/p=enter the browser name
edge
enter the value of a number
1900
the year is not leap year'''
