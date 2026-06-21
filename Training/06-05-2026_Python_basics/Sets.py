# SETS --- DOES NOT ALLOW DUPLICATES

Numbers = {10, 20, 30, 40}
print(Numbers)

Numbers = {10, 20, 30, 40, 40,}
print(Numbers)

#ADD
Numbers.add(50)
print(Numbers)

Numbers.remove(50)
print(Numbers)

for num in Numbers:
    print(num)

print(len(Numbers))

# Sets  Union, intersection, difference

set1 = {1, 2, 3}
set2 = {4, 5, 6}

#Union

result = set1.union(set2)
print(result)

result = set2.union(set1)
print(result)

##Intersection
result = set1.intersection(set2)
print(result)

result = set2.intersection(set1)
print(result)

##Difference

result = set1.difference(set2)
print(result)

result = set2.difference(set1)
print(result)

##List to set
Numbers = [1,2,2,3,3,3,4,5,6,7,8,9,9,9,]
UniqueNumbers = set(Numbers)
print(UniqueNumbers)
