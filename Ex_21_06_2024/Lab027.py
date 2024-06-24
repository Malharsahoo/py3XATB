# conversion of list to tuple using tuple function
'''my_list=[1,2,3,4,5]
t1=tuple(my_list)
print(t1)
print(t1[2]) '''
# now t1 is the tuple. o/p= (1, 2, 3, 4, 5) & 3


#we can have tuple within tuple too... lets we have two items tuples
'''hero1=("hrithik","shahrukh")
hero2=("shahid","salman")
new_tuple=(hero1,hero2)
print(new_tuple)'''
#o/p=(('hrithik', 'shahrukh'), ('shahid', 'salman'))

'''print(new_tuple[0][1])'''
#o/p= shahrukh

'''print(new_tuple[1][0])'''
#o/p= shahid

'''print(new_tuple[1][1])'''
#o/p= salman

'''print(new_tuple[0][0])'''
#o/p= hrithik


# we can also assign values to variables using tuple
''' a,b,c=(10,20,30)
print(a)
print(b)
print(c) '''
#o/p= 10
#20
#30


#we can also do search in tuple using in
''' cities=("delhi","bangalore","mumbai","chennai")
print("delhi" in cities)'''
#o/p= True

'''print("kolkata"in cities)'''
#o/p= False



# adding a new element to tuple. append is not allowed in tuple
''' tuple=(11,12,13,14)
new_tuple=tuple+(7,)
print(new_tuple) '''
#o/p=(11, 12, 13, 14, 7)


# we can also convert tuple to list then append value to list then again convert list to new tuple
tuple1=(1,2,3,4)
my_list=list(tuple1)
my_list.append(10)
new_tuple= tuple(my_list)
print(new_tuple)