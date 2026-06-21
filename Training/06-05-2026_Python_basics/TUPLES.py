Numbers = (10, 20, 30, 40, 50)

print(Numbers)

print(Numbers[0])
print(Numbers[1])
print(Numbers[2])

print(Numbers[-1])
print(Numbers[-2])

print(Numbers[1:5])

# YOU CANT MODIFY TUPLES --- THEY ARE IMMUTABLE
#
# Numbers[1] = 99
# print(Numbers[1])

for num in reversed(Numbers):
    print(num)


