#
#
# #1. Find second largest number
# a = [10, 20, 4, 45, 99]
#
# print(a)
# largest = second = float('-inf')
# for n in a:
#     if n > largest:
#         second = largest
#         largest = n
#     elif n > second and n !=largest:
#         second = n
# print (second)
#
#
# #2. Rotate List to Right by K Steps
#
# nums = [1,2,3,4,5]
# print(nums)
# k = 2
#
# k = k % len(nums)
# nums = nums[-k:] + nums[:-k]
#
# print(nums)
#
# #3. Find missing number(1 to n)
#
# nums = [1,2,3,5]
# n = 5
#
# expected_sum = n * (n+1) // 2
# actual_sum = sum(nums)
#
# missing_number = expected_sum - actual_sum
# print(missing_number)
#
# #4. Move all zeroes to end
# nums = [0, 1, 0, 3, 12]
# pos = 0
#
# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[pos], nums[i] = nums[i], nums[pos]
#         pos += 1
#
# print(nums)
#
# #5. Find pairs with given sum
#
# nums = [2, 4, 3, 5, 7, 8]
# target = 7
#
# seen = set()
# for num in nums:
#     diff = target - num
#     if diff in seen:
#         print(diff, num)
#     seen.add(num)
#
# # TUPLES
# #6. Sort list of tuples by second value
#
# data = [(1,3), (2,1), (4,2)]
#
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)
#
# #7. Convert tuples list into Dictionary
#
# tuples = [(1,"Siva"),(2,"ganesh")]
# result = dict(tuples)
# print(result)
#
# #SETS
#
# #8. Find unique elements from two lists
#
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
#
# unique_elements = list(set(list1) ^ set(list2))
# print(unique_elements)
#
# #9. Check if two lists have common elements
#
# list1 = list(map(int,input("Enter a list1 elements: ").split()))
# list2 = list(map(int,input("Enter a list2 elements: ").split()))
#
# if set(list1)&set(list2):
#     print("Common element exists")
# else:
#     print("Common element does not exist")
#
# #DICTIONARIES
#
# #10. Count frequency of elements
#
# nums = [1, 2, 2, 3, 3, 3]
# freq = {}
# for num in nums:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)
#
# #11.Find key with max value
#
# nums = {"a":10,"b":25, "c":15}
#
# max_key = max(nums, key = nums.get)
# print(max_key)
#
# #12. Merge two Dictionaries
#
# d1 = {"a":1, "b":2}
# d2 = {"b":3, "c":4}
#
# merged = {**d1, **d2}
# print(merged)
#
# #13. Invert a Dictionary
#
# d1 = {"a":1, "b":2}
#
# inverted = {v : k for k, v in d1.items()}
# print(inverted)
#
# # SECTION 5 - COMBINED
#
# #14. GROUP ELEMENTS BY FREQUENCY
#
# nums = [1, 1, 2, 2, 2, 3]
#
# result = {}
#
# for n in nums:
#     if n in result:
#         result[n].append(n)
#     else:
#         result[n] = [n]
# print(result)
#
# #15. Find first non-repeating element
#
# nums = [4, 5, 1, 2, 0, 4]
#
# freq = {}
#
# for num in nums:
#     freq[num] = freq.get(num, 0) + 1
#
# for num in nums:
#     if freq[num] == 1:
#         print(num)
#         break
#
# #16. Flatten nested list
#
# nested_list = [[1,2], [3,4],  [5]]
#
# flat_list = [item for sublist in nested_list for item in sublist]
# print(flat_list)
# ------------------------------------------------------------------------------------
#
# #Iteration
#
# numbers = [10, 20, 30, 40, 50]
# it = iter(numbers)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# ----------------------------------------------------------------------------------------
#
# #GENERATOR

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
# gen = my_generator()
# for num in gen :
#     print(num)
#-----------------------------------------------------------------------------------------------

#Decorator

# def my_decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper
#
# # @my_decorator
# def say_hello():
#     print("Hello")
# decorated = my_decorator(say_hello)
# decorated()
#----------------------------------------------------------------------

#
# # regular function
# def add(a, b):
#     return a + b
#
# print(add(5,4))
#
# #lambda function
#
# add = lambda a, b : a + b
# print(add(5,4))
#------------------------------------------------------------

#squares

# numbers = [1, 2, 3, 4]
#
# squares = list(map(lambda x: x*x, numbers))
# print(squares)
# ---------------------------------------------------------------------
# # even numbres
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = list(filter(lambda x: x % 2 == 0, numbers))
# print(even)
# ----------------------------------------------------------------------

# reduce

# numbers = [1, 2, 3, 4]
#
# result = reduce(lambda a, b: a + b, numbers)
# print(result)
#
# ------------------error-------

