# gradient = 1
#
# for i in range(10):
#     gradient = gradient * 0.1 #Grading is vanishing
#
#     print(f"{gradient:.10f}")
#---------------------------------------------------
gradient = 1

for i in range(10):
    gradient = gradient * 0.1 + 1  #Grading is vanishing

    print(f"{gradient:.10f}")