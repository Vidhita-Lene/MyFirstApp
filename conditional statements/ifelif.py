# day=int(input("enter a number"))
# if(day==1):
#     print("monday : study time")
# elif(day==2):
#     print("tuesday: relax time")
# elif(day==3):
#     print("wednesday: travel time")
# elif(day == 4):
#     print("thursday: party time")
# elif(day==5):
#     print("friday: revision day")
# elif(day==6):
#     print("saturday: hobby day")
# else:
#     print("enter valid number")

#wrie a python program which displays number of days in that particular month
month=int(input("enter a month number:"))
if(month==1 or month==3 or month== 5 or month==7 or month==9 or month==11):
    print( f"{month} has 31 days")
elif(month==4 or month==6 or month==8 or month==10 or month==12):
    print(f"{month} has 30 days")
elif(month==2):
    print(f"{month} has 28 days")
else:
    print("month not found")