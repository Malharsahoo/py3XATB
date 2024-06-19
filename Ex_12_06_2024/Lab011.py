#  take score as input and grade it according to the category
# 0-59_A, 60-69_B, 70-79_C, 80-89_B, 90-100_A, other than is invalid score

num=int(input("enter the score\n"))
if num>= 90 and num<=100:
    print("your  grade is: A ")
elif num>=80 and num<=89:
    print("your grade is: B")
elif num>=70 and num<=79:
    print("your grade is: C")
elif num>=60 and num<=69:
    print("your grade is: D")
elif num>=0 and num<=59:
    print("your grade is : FAIL")
else:
    print("invalid score")