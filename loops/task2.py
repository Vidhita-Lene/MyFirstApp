# 1.Write a Python program to find those numbers which are divisible by 7 and 5, between range 1500 and  
#2700 (both included). -> Create an empty list to store numbers that meet the given conditions.

# empty_list=[]
# for i in range(1500,2700):
#     if(i%5==0 and i%7==0):
#         empty_list.append(i)
# print("numbers divisible by 5 and 7 are:\n",empty_list)

#2.. Write a Python program that displays a menu with three options: 
# 1. Addition 
# 2. Subtraction 
# 3. Multiplication
#while(1)
# int Choice
# switch(choice)
print("select option 1,2,3\n")
print("1.addition,\n2subtraction,\n3multiplication\n")
print("enter choice:")
choice=int(input())
if(choice==1):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    result=a+b
    print("addition is:",result)
elif(choice==2):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    result=a-b
    print("subtraction is:",result)
elif(choice==3):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    result=a*b
    print("multiplication is:",result)
else:
    print("invalid choice")