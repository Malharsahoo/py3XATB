# all methods of list
# list is nothing but collection of items

my_list1=[1,2,3]
my_list2=[1,True,"sipu",12.34]
#print("Element at index 0:",my_list1[0])
#o/p-Element at index 0: 1


#changing an element
my_list1[1]=20
print("list after changing element at index 1:",my_list1)
#o/p=list after changing element at index 1: [1, 20, 3]

# append()
my_list1.append(4)
print("list after appending is:",my_list1)
#o/p=list after appending is: [1, 20, 3, 4]


#extend()
my_list1.extend([5,6])
print("list after extending is:",my_list1)
#o/p=list after extending is: [1, 20, 3, 4, 5, 6]


#insert()
my_list1.insert(1,"a")
print("list after inserting 'a' in index 1 is:",my_list1)
#o/p=list after inserting 'a' in index 1 is: [1, 'a', 20, 3, 4, 5, 6]


#remove()
my_list1.remove("a")
print("list after removing 'a' is:",my_list1)
#o/p= list after removing 'a' is: [1, 20, 3, 4, 5, 6]


# copy() list
my_copy_list1=my_list1.copy()
print("list after copying is:",my_copy_list1)



#clear()
my_list1.clear()
print("initial list is",my_list1)
print(my_copy_list1)
#o/p= initial list is []
#[1, 20, 3, 4, 5, 6]


#reverse()
my_copy_list1.reverse()
print(my_copy_list1)
#[6, 5, 4, 3, 20, 1]


#sort()
my_copy_list1.sort()
print(my_copy_list1)
#[1, 3, 4, 5, 6, 20]

