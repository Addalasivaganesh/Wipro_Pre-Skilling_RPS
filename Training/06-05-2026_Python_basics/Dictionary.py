# # Dictionary
#
# Student = {
#     'Name': 'Siva',
#     'Age': 20,
#     'course': 'Python'
# }
# print(Student)
#
# print(Student['Name'])
# print(Student['Age'])
# print(Student['course'])
#
# #Add a new key value pair
# Student["city"] = "HYDERABAD"
# print(Student)
#
# #update the data
# Student["Age"] = 23
# print(Student)
#
# del Student["city"]
# print(Student)
#
#
Student = {
    "Name": "Siva ganesh addala",
    "age": "23",
    "City": "HYDERABAD"
}

#keys Iteration
for key in Student:
    print(key)

#Value iteration
for value in Student.values():
    print(value)

#;loop through key value pairs

for key, value in Student.items():
    print(key, value)

print(Student)