set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

#Accessing is not possble 

#Updating the sets
set1.update({5, 6})
print(set1) 

#Removing an elemnent
set1.pop()
print(set1)

#max and minimum value 
print(max(set1))
print(min(set1))

#sort
print(sorted(set1))

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

#union
print(set1.union(set2))

#inersection
print(set1.intersection(set2))

#subtraction
print(set1 - set2)
print(set2 - set1)