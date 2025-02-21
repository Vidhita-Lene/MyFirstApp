#union #intersection #diffeence
set1={2,4,6,8,10}
set2={1,2,3,4,5,6,7}
#union : | (pip) operator
set3=set1|set2
print("using | (pip operator)",set3)

#union using union method
set3=set1.union(set2)
print("using union method",set3)

#intersection: using & operator
set3=set1&set2
print("using & operator",set3)

#intersection using intersecton operator
set3=set1.intersection(set2)
print("using intersection method",set3)

#diffrence method  using - opertor
set3=set1-set2
print("using - operator",set3)

set4=set2-set1
print(set4)

#diffrence using difference method
set5=set1.difference(set2)
print(set5)