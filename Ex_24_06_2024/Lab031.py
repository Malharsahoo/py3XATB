my_dict={
    "a":2,
    "b":3,
    "c":4,
    "d":5
}
for k,v in my_dict.items():
    if k=="b":
        print("key values of b is found")


m="b" in my_dict
print(m)
#key values of b is found
#rue
