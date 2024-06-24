# Dictionary       key-values pair

''' my_dict2={"name":"sipu",
          "age":10,
          "city":"Bangalore"
         }
print(len(my_dict2))
print(my_dict2["name"])
print(my_dict2["age"])
print(my_dict2["city"]) '''

#o/p= 3
#sipu
#10
#Bangalore


# we can also do without double quotes using keyword dict
''' my_dict3=dict(name="sipu",age=45,city="delhi")
print(my_dict3)
print(len(my_dict3))
print(my_dict3["age"])
print(my_dict3["name"]) '''
#o/p={'name': 'sipu', 'age': 45, 'city': 'delhi'}
#3
#45
#sipu


#dict is mutable. we can change anything
'''my_dict3=dict(name="sipu",age=45,city="delhi")
my_dict3["name"]="kunja"
print(my_dict3)'''
#o/p={'name': 'kunja', 'age': 45, 'city': 'delhi'}


#get function get(). we can get the value of a dictionary also using get()
'''sipu_details= \
    {"name":"sipu",
     "alter_name":"malhar",
     "age":65,
    "isMale":True,
     "address":"karnataka",
     "90":30.34
    }
print(sipu_details.get("address"))
print(sipu_details["name"])'''  # we can use [] also to get the value
#o/p=karnataka
#    sipu


# we can get all values and keys too
'''print(sipu_details.values())
print(sipu_details.keys())'''
#dict_values(['sipu', 'malhar', 65, True, 'karnataka', 30.34])
#dict_keys(['name', 'alter_name', 'age', 'isMale', 'address', '90'])



# key can't be duplicated but values can be duplicated
'''my_dict={"a":2,"b":2,"c":3,"d":4,"e":5,"c":9}
print(len(my_dict))
print(my_dict)'''
#o/p=5
#{'a': 2, 'b': 2, 'c': 9, 'd': 4, 'e': 5}


#we can convert keys to list and values to list too
'''my_dict={"a":1,"b":2,"c":3,"d":4}
print(list(my_dict.keys()))
#o/p=['a', 'b', 'c', 'd']
print(list(my_dict.values()))
#o/p=[1, 2, 3, 4]'''


#after converting dictionary to list, we can go to key or values one by one
''' my_dict={"a":1,"b":2,"c":3,"d":4}
my_key_list=list(my_dict.keys())
for i in my_key_list:
    print(i) '''
#o/p=a
#b
#c
#d
''' my_values_list=list(my_dict.values())
for i in my_values_list:
    print(i) '''
#o/p=1
#2
#3
#4


#single way to get key and values pair in dictionar
''' my_dict={"a":1,"b":2,"c":3,"d":4}
for k,v in my_dict.items():
    print(k,v) '''
#a 1
#b 2
#c 3
#d 4




