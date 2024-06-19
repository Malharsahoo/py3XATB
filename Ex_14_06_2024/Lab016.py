def allowed_to_attend_python_class(name,password):
    if name=="sipu":
        if password=="yes":
            print("you are allowed to attend")
        else:
            print("you are not allowed")
allowed_to_attend_python_class("sipu","no")

#o/p= you are not allowed