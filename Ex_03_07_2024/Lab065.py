''' suppose we want to read the files dont as a list but as line by line then we can use
     for loop for that '''

with open("sipu.txt","r") as file:
    content=file.readlines()

for line in content:
    print(line,end=" ")

file.close()




# o/p= this is for example of lab058
#  hello sipu
#  hello sipu
#  hope you are doing well
#  hello sipu
#  hope you are doing well
#
#  #  hellooooo
#
#
#  #hiiiiiiii
#
#  #youuuuuuuuuhello sipu
#  hope you are doing well