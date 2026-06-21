numbers = [1,2,3,4,5]

#list_comprehension
squares = [x*x for x in numbers]
print(squares)

#list_comprehension with condition
even = [x for x in numbers if x % 2 == 0]
print(even)

#list of strings
names = ["a.siva", "ganesh"]
upper_names = [name.upper() for name in names]
print(upper_names)
