#1. What is the output of the following code? 
lst = [1, 2, 3, 4, 5]  
print(lst[::-1]) 
#output:[4,3,2,1]

#2.What will be printed? 
lst = [10, 20, 30]  
lst.append([40, 50])  
print(len(lst)) 
#output:4

#3.Predict the output: 
lst = [1, 2, 3]             
lst.extend([4, 5])          #[1,2,3,4,5]  extend
lst.insert(2, 10)           #1,2,10,3,4,5   insert
print(lst)
#output:1,2,10,3,4,5 

#4. What is the output of this code? 
tup = (1, 2, 3, 4) 
tup[2] = 10 
print(tup) 
#output:(1,2,10,3,4)

# 5.Find the output: 
tup = (10, 20, 30, 40, 50) 
print(tup[-3:])
#output:(50,40,30)

#6.Find the output: 
set1 = {1, 2, 3} 
set2 = {2, 3, 4} 
print(set1 & set2)
#output:{2,3}

#7. Find the missing code to get the correct difference between two sets: 
set1 = {10, 20, 30, 40} 
set2 = {30, 40, 50, 60} 
diff = set1-set2            
print(diff)   
#output: missing value= set1-set2

#8.What will be printed? 
d = {'x': 10, 'y': 20} 
d['z'] = 30 
print(d)   
#output:  {'x': 10, 'y': 20,'z':30}    

#9. What will be printed? 
d = {'a': 1, 'b': 2, 'c': 3} 
d.pop('b') 
print(d) 
#output: {'a': 1,'c': 3} 