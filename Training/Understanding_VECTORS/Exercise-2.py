import numpy as np

salary = np.array([25000, 30000, 45000, 50000])
print("Original salary", salary)

#increasing salary by 10%
Increased_salary = salary * 1.10
print("After 10% increment",Increased_salary)

#find highest salary
print("MAximun number", np.max(salary))

#find lowest salary
print("Minimum number", np.min(salary))

#find total salary payout
print("TOTAL_SALARY", np.sum(salary))