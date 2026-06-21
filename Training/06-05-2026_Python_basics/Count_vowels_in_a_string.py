a = input("Enter a string: ")
vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]
count = 0

for char in a:
    if char in vowels:
        count += 1
print("Number of vowels in a string are : ", count)