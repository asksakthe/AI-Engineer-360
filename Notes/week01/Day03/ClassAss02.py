def calculate_salary(basic, hra, da, bonus=0):
	return basic + hra + da + bonus

# Calling without bonus
salary1 = calculate_salary(30000, 8000, 5000)
print("Salary (without bonus):", salary1)
# Calling with bonus
salary2 = calculate_salary(30000, 8000, 5000, 2000)
print("Salary (with bonus):", salary2)

# def calci(*args):
# 	sal = 0
# 	sal += args
# 	return sal

# salary3 = calci(30000, 8000, 5000, 2000)
# print("Salary 3 (with bonus):", salary3)
