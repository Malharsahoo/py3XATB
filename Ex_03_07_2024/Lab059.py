class XYZ:
    def f1(self):
        try:
            a=int(input("enter a number\n"))
        except Exception as e:
            print("enter int only as value of a")
        else:
            print(a)
        finally:
            print("anyhow i will be printed")
s=XYZ()
s.f1()


#o/p=  enter a number
#      5
#      5
#      anyhow i will be printed


# o/p= enter a number
#      sipu
#      enter int only as value of a
#      anyhow i will be printed