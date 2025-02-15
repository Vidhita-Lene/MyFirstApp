sentence='hi, i am learning python and i am good'
print('capitalize method:', sentence.capitalize())
print('upper method:', sentence.upper())
print('title method:', sentence.title())
print('-'*50)
count_method=sentence.count('h')
print('count method:',count_method)
print('-'*50)
#split method
split_method=sentence.split()
print('split method:',split_method)
print('-'*50)
#index method
index_method= sentence.index('i')
print('index method:',index_method)
print('-'*50)
replace_method=sentence.replace('python','java')
print('replace method:',replace_method)
print('-'*50)
print('sentence:',split_method)
join_method = '&'.join(split_method)
print('join method:',join_method)
print('-'*50)

var='vidhi'
isalpha_method=var.isalpha()
print('isalpha method:',isalpha_method)
print('-'*50)

var_1='vidhi1904'
numer_method=var_1.isalnum()
print('is alpha numeric:',numer_method)
print('-'*50)

var_2='vidhi@' #when special symbol added then only it gives false
numermethod=var_2.isalnum()
print('is alpha numeric:',numermethod)
print('-'*50)

var_3='123456'
numermethod=var_3.isalnum()
print('is alpha numeric:',numermethod)