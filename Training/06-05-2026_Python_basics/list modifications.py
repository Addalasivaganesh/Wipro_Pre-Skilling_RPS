# for commenting bulk lines use ctrl /

Numbers = [10, 20, 30, 40, 50]

print(Numbers)

print(Numbers[0])
print(Numbers[1])
print(Numbers[2])
print(Numbers[3])
print(Numbers[4])

#Negative indexing

print(Numbers[-1])
print(Numbers[-2])
print(Numbers[-3])
print(Numbers[-4])
print(Numbers[-5])

#modifying list elements

Numbers[1] = 99
print(Numbers)

#Adding elements to list
Numbers.append(60)
print(Numbers)

Numbers.insert(1,26)
print(Numbers)

Numbers.remove(99)  # Remove the particular number
print(Numbers)

Numbers.pop() # Remove  last number
print(Numbers)

print(len(numbers))

for num in Numbers:
    print(num)

#slicing
Numbers = [10, 20, 30, 40, 50]
print(Numbers[1:4])