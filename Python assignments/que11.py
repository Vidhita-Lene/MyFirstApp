#2.. Write a Python program that displays a menu with three options: 
# 1. Addition 
# 2. Subtraction 
# 3. Multiplication

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