                                         # OS  MODULE

#get current working directory
#import os
#print(os.getcwd())
#o/p=C:\Users\Admin\PycharmProjects\py3XATB\ex_05july\Ex_05_07_2024


#change the directory
'''import os
os.chdir("C:\\Users\\Admin\\PycharmProjects\\py3XATB\\ex_05july\\")
print(os.getcwd())'''
#o/p= C:\Users\Admin\PycharmProjects\py3XATB\ex_05july


# list the directory
'''import os
print(os.listdir("C:\\Users\\Admin\\PycharmProjects\\py3XATB\\ex_05july\\"))'''
# o/p= ['Ex_01_07_2024', 'Ex_03_07_2024', 'Ex_05_07_2024']


#making a new directory
'''import os
os.mkdir("sipu")'''


#size of file though os
'''import os
size=os.path.getsize("TestData.txt")
print(size)'''
#o/p= 53 (in bytes)


# modification time of file
'''import os
mo_time=os.path.getmtime("TestData.txt")
print(mo_time)'''
# o/p= 1720866726.2631073     (this is usually in float and it is called Epoch Time


#Setting an environment variable
'''import os
os.environ["my_var"]="sipu"
print(os.getenv("my_var"))'''
#o/p= sipu


#           walk through directory
''' import os
for root,dir,files in os.walk("C:\\Users\\Admin\PycharmProjects\\py3XATB\\ex_05july\\Ex_05_07_2024\\"):
    print(f"current directory is {root}")
    print(f"sub directory is {dir}")
    print(f"files in directory is {files}")'''
# o/p = current directory is C:\Users\Admin\PycharmProjects\py3XATB\ex_05july\Ex_05_07_2024\
     # sub directory is ['kunja', 'sipu']
     # files in directory is ['Lab068.py', 'TestData.txt']
     # current directory is C:\Users\Admin\PycharmProjects\py3XATB\ex_05july\Ex_05_07_2024\kunja
     # sub directory is []
     # files in directory is []
     # current directory is C:\Users\Admin\PycharmProjects\py3XATB\ex_05july\Ex_05_07_2024\sipu
     # sub directory is []
     # files in directory is ['sipu.txt']


# read and write to files
import os
rw=os.open("TestData.txt",os.O_RDWR)
os.write(rw,b" I am currently writting")
os.close(rw)
