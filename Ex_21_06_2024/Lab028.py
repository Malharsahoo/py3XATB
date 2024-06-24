#SET is collection of items.we can say unique items(remove duplicate) in unordered way
'''  list_of_items={1,2,3,4,4,5,5,5,6,66}
print(list_of_items)  '''
#o/p={1, 2, 3, 4, 5, 6, 66}

#conversion of list to set
''' my_list=[1,2,3,4,4,5,55,5,6,77,7,4]
new_list=set(my_list)
print(new_list)
print(len(new_list)) '''
#o/p={1, 2, 3, 4, 5, 6, 7, 77, 55} & 9


#conversion of tuple to set
''' tuple1=("The hindu","for","The hindu")
print(set(tuple1))
print(len(set(tuple1))) '''
#o/p={'The hindu', 'for'} & 2


#union property of SET
''' set1={1,2,3}
set2={4,5,6}
my_set=set1.union(set2)
print(my_set)  '''
#{1,2,3,4,5,6}


#intersection property of set
''' set1={1,2,3,4,5,6}
set2={5,6,7,8,1,9}
my_set=set1.intersection(set2)
print(my_set) '''
#{1, 5, 6}


#difference property of set
''' set1={1,2,3,4,5,6}
set2={5,6,7,8,1,9}
my_set=set2.difference(set1)
print(my_set) '''
#o/p={2, 3, 4}


#subset property of set
'''  set1={1,2,3,4,5,6}
set2={2,3,4}
my_set=set2.issubset(set1)
print(my_set)  '''
#o/p= True


#remove function in set
'''  set1=set([1,2,3,4,5,6,7,8])
print(len(set1))
#o/p=8
set1.remove(5)
print(set1)
print(len(set1))  '''
#{1, 2, 3, 4, 6, 7, 8}  & 7

#add
set1=set([1,2,3,4,5,6])
set1.add(100)
print(set1)
#o/p={1, 2, 3, 4, 5, 6, 100}


#pop() randomly remove item but generally remove first one.
set1=set([1,2,3,4,5,6])
set1.pop()
print(set1)
#o/p={2,3,4,5,6}


