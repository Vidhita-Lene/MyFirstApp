#string- its sequence of characters
#it is enclosed in single,double and for multiple lines triple quotes
#return type: str
#immutable

#creating a string
#statement_1= 'today is thursday'
#statement_2= "today is thursday"
#print('string:',statement_2)
#print('string type:',type(statement_2))
#print('length of string:',len(statement_2))
#print('accessing value at 0th position', statement_2[0])
#print('accessing value at 1th position', statement_2[1])
#print('accessing value at 2th position', statement_2[2])
#print('accessing value at 3th position', statement_2[3])
#print('accessing value at 4th position', statement_2[4])
#print('accessing value at 5th position', statement_2[5])

#same statement with different quotes
time= "It's 6.30pm"
print('same quotes:',time)
print('accessing value at 0th position', time[0])
print('accessing value at 1th position',time[1])
print('accessing value at 2th position', time[2])
print('accessing value at 3th position', time[3])
print('-'*50)

#escape sequence/escape character: \,\n,\t
time= "It\"s 6.30pm"
print('double quotes:',time)
print('accessing value at 0th position', time[0])
print('accessing value at 1th position',time[1])
print('accessing value at 2th position', time[2])
print('accessing value at 3th position', time[3])

#concatination"
Full_name= "disha roy"
age= 27
#print('my name is'+' '+Full_name+'i am'+' '+age)
print('my name is'+' '+Full_name+'i am'+' '+str(age))
