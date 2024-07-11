import csv
with open("example.csv") as csvfile:
    reader=csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],sep="||")



# o/p= user||password
# admin||password
# admin||user
# admin||admin123
# user123||user
# password||user123
