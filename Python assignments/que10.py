 #1.Write a Python program to find those numbers which are divisible by 7 and 5, between range 1500 and  
#2700 (both included). -> Create an empty list to store numbers that meet the given conditions.

empty_list=[]
for i in range(1500,2700):
   if(i%5==0 and i%7==0):
        empty_list.append(i)
print("numbers divisible by 5 and 7 are:\n",empty_list)