#0-10
# count=0
# while(count<=10):
#     print(count)
#     count=count+1

#display 13-45 range of numbers.
# count=13
# while(count<46):
#     print(count)
#     count=count+1

#display even numbers between range 20-36
# count=20
# while(count<=36):
    
#     if(count%2==0):
#         print(count)
#     count=count+1
    
#display reverse of above even numbers
# count=36
# while(count>=20):
#     if(count%2==0):
#         print(count)
#     count=count-2


#write a python program to display sum of digits of a number
num=int(input("enter a number"))
sum=0
while(num>0):
    remainder=num%10
    sum=sum+remainder
    num=num//10
print("sum of digits of a number=",sum)