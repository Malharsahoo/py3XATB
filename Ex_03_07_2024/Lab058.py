''' in finally also we can handle if the file is not found'''

#with open("sipu.txt","r") as file:
#    print(file.read())
#    '''we can read the content of the any text file with the above two lines of code'''
#    file.close()      # we always need to close the file to save the memory after opening it.

 # o/p= this is for example of lab058 & Lab059



 # lets say we change the name of the file as malhar.txt
'''with open("malhar.txt","r") as file:
    print(file.read())
    file.close()'''
# then we will get error as FileNotFoundError: [Errno 2] No such file or directory: 'malhar.txt'
'''so we need to handle this error'''

''' in finally also we can handle this error if the file is not found'''

import os.path
try:
    file=open("malhar.txt","r")
    print(file.read())
except FileNotFoundError as fnfe:
    print("i am not able to find the file")
finally:
    print("executed")
    try:
       file.close()
    except NameError as ne:
        print(ne)


# o/p= i am not able to find the file
#      executed
#      name 'file' is not defined

