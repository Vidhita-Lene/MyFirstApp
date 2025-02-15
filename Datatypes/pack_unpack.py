emp_details=('rahul',124,15000,'admin')  #pack
(name,jobid,salary,jobrole)=emp_details  #unpack
print(jobid)

emp_details=('rahul',124,15000,'admin','trainer')
(name,jobid,salary,*jobrole)=emp_details
print(jobrole)