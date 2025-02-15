week={'monday':'holiday','tuesday':'workdone','wednesday':'learning python'}
# methods:keys, values, items
#update method:
week.update({'thursday':'holiday'})
print('update method:', week)

print('-'*50)

#get method- access value of given key
get_method=week.get('wednesday')# wednesday is given as key and
print('get method:',get_method)# get returned value as learning python
print('-'*50)

#pop method
week.pop('wednesday')
print('pop method:', week)
print('-'*50)

#popitem method
week.popitem()
print('popitem method:',week)