# List Data Type & ADD, REMOVE,UPDATE, VIEW,,EXTEND, SORTING, REVERSING,

my_list=["milk","chocolate","rice","fruits",-23,0,5,True,5.89]
print(len(my_list))
print(type(my_list))
# results= 9 & list


print(my_list[1])
print(my_list[-2])
# results= chocolate & True


# append means adding item to the list end
my_list.append("juice")
print(my_list)
#['milk', 'chocolate', 'rice', 'fruits', -23, 0, 5, True, 5.89, 'juice']


#inserting item to the list by index value
my_list.insert(3,"sugar")
print(my_list)
#results=['milk', 'chocolate', 'rice', 'sugar', 'fruits', -23, 0, 5, True, 5.89, 'juice']


#extended items list
my_list.extend(["onions","garlic"])
print(my_list)
#result=['milk', 'chocolate', 'rice', 'sugar', 'fruits', -23, 0, 5, True, 5.89, 'juice', 'onions', 'garlic']


#remove an item from the list end
my_list.pop()
print(my_list)
#result=['milk', 'chocolate', 'rice', 'sugar', 'fruits', -23, 0, 5, True, 5.89, 'juice', 'onions']


# index of an item from the list
print(my_list.index("sugar"))
# result=3

#reverse of the list
my_list.reverse()
print(my_list)
#result=['onions', 'juice', 5.89, True, 5, 0, -23, 'fruits', 'sugar', 'rice', 'chocolate', 'milk']


#sorting of the list
my_list=["milk","chocolate","rice","fruits"]
my_list.sort()
print(my_list)
#results=['chocolate', 'fruits', 'milk', 'rice']


#it is mutable sequence means we can change the item by replacing it with new one by index value
my_list[2]="John"
print(my_list)
#results=['chocolate', 'fruits', 'John', 'rice']