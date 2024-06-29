# filters
'''my_list=[1,2,3,4,5,6,7,8,9,10,8,11,12]

def is_even(num):
    return num%2==0

new_even_num_list=filter(is_even,my_list)
print(list(new_even_num_list))'''
#[2, 4, 6, 8, 10, 8, 12]


# filter out greater than 5 elements from the my list
'''my_list=[1,2,3,4,5,6,7,8,9,10,8,9,11,12]
def greater_than_five(num):
    return num>5
new_greater_than_five=filter(greater_than_five,my_list)
print(list(new_greater_than_five))'''
#o/p=[6, 7, 8, 9, 10, 8, 9, 11, 12]