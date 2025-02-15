#collection of key:value pairs
#ordered/mutable
#key unique

watch_details={'titan':5000,
'fastrack':6000,
'sonata':4000,
'omega':4000
}
print("dictionary:",watch_details)
print("dictionary length:",len(watch_details))
print("dictionary type:",type(watch_details))
print("using key value access:", watch_details['titan'])
watch_details['omega']=True
print("changing value:",watch_details)

print('-'*50)
#method
#keys
print('key method:',watch_details.keys())
print('value method:',watch_details.values())
print('item method:',watch_details.items())
