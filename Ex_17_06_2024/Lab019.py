# there are multiple ways to call a function

def sum_of_three(a=1,b=2,c=3):
    return a+b+c
res1=sum_of_three()
res2=sum_of_three(5,7)
res3=sum_of_three(9,8,4)
res4=sum_of_three(a=12,b=15,c=10)
res5=sum_of_three(b=10,c=15,a=11)
print(res1,res2,res3,res4,res5)
#O/P=6 15 21 37 36