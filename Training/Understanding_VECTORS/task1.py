import numpy as np

marks = np.array([ 85, 90, 78])

#print the vector
print("Marks :", marks)

#Add 5 bonus marks
bonus_marks = marks + 5
print("After adding bonus_marks: ", bonus_marks)

#Multiply marks by 2
Double_marks = marks * 2
print("After multiplying Double_marks: ", Double_marks)

#Finding average marks
avg = np.mean(marks)
print("average of given numbers are :", avg)