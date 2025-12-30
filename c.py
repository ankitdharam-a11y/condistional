m=input("Do you have the medical report yes or no")
a=int(input("your attendence is greater than 5 yes or no"))
if m=='yes':
    print("you are allowed")
else:
    if a>=75:
        print("you are allowed")
    else:
        print("you are not allowed")