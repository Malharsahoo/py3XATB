num=[1,2,3]
def do_something(num):
    num.append(4)
    num[0]=100
    return num
l=do_something(num)
print(l)
