#doubling the elements present in the list

#            -----------M1-----------
'''my_list=[1,2,3,4,5]
double_list=[]
for i in my_list:
    double=i*2
    double_list.append(double)
print(double_list)'''
#o/p=[2, 4, 6, 8, 10]



#           --------------M2-----------
'''my_list=[1,2,3,4,5]
double_list=[]
for i in list1:
    double_list.append(i*2)
print(double_list)'''
#o/p=[2,4,6,8,10]




#            ---------------M3---------------
my_list=[1,2,3,4,5]
'''def double_list(number):
    return number*2
new_list=list(map(double_list,my_list))
print(new_list)'''
#o/p=[2, 4, 6, 8, 10]


#           ---------M4----------
#using lambda and map square the list items
'''my_list=[1,2,3,4,5]
double_item=lambda num:num*2
double_list=list(map(double_item,my_list))
print(double_list)'''
#o/p=[2,4,6,8,10]



#              --------M5-------
'''my_list=[1,2,3,4,5]
double_list=list(map(lambda num:num*2,my_list))
print(double_list)'''
#o/p=[2,4,6,8,10]



#             -------M6------
'''my_list=[1,2,3,4,5]
print(list(map(lambda num:num*2,my_list)))'''
# o/p= [2,4,6,8,10]


#             -------------M7--------------
print(list(map(lambda num:num*2,[1,2,3,4,5])))
#o/p=[2,4,6,8,10]