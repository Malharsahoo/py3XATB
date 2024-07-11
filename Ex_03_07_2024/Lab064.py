# suppose we have multiple lines and we want to read them
with open("sipu.txt","r") as file:
    content=file.readlines()
    print(content)

file.close()

# o/p= ['this is for example of lab058\n', 'hello sipu\n', 'hello sipu\n', 'hope you are doing well\n', 'hello sipu\n', 'hope you are doing well\n', '\n', '#  hellooooo\n', '\n', '\n', '#hiiiiiiii\n', '\n', '#youuuuuuuuuhello sipu\n', 'hope you are doing well\n']