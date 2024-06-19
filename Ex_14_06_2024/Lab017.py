# you are allowed to enter if your name matches using match case and function

def allowed_to_enter(name):
    match name:
        case "sipu":
              print(" sipu is allowed to enter the class")
        case "radhika":
              print("radhika is allowed to enter the class")
        case "shilpa":
              print("shilpa is allowed to enter the class")
        case _:
              print("you are not allowed")
allowed_to_enter("kunja")



#o/p1: radhika is allowed to enter the class
#o/p2: you are not allowed