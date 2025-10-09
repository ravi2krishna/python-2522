# Operators in python 

# Arithmetic Operators 
num1 = 10
num2 = 5

print(f"Sum of {num1} and {num2} is {num1+num2}")
print(f"Difference of {num1} and {num2} is {num1-num2}")
print(f"Product of {num1} and {num2} is {num1*num2}")
print(f"Division of {num1} and {num2} is {num1/num2}")
print(f"Modulus of {num1} and {num2} is {num1%num2}")

num1 = 3
num2 = 2

# Floor Division
print(f"Normal Division of {num1} and {num2} is {num1/num2}")
print(f"Floor Division of {num1} and {num2} is {num1//num2}")

# Exponentiation
print(f"Exponentiation Division of {num1} and {num2} is {num1**num2}")


# Compound Assignment Operators
num = 10
# Without Compound Assignment Operators
num = num + 5 
print(num)

num = 10
# With Compound Assignment Operators
num += 5 
print(num)

# increment 
count = 1
# count++ 
count += 1
print(count)

# decrement 
count = 10
# count++ 
count -= 1
print(count)

# Comparison Operators
num1 = 10
num2 = 5
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)

# Logical Operators
num1 = 10
num2 = 5
num3 = 3
num4 = 15
print("==============")
result_and = num1 > num2 and num3 < num4 # T and T -> T
print(result_and)
result_and = num1 < num2 and num3 < num4 # F and T -> F
print(result_and)
print("==============")
result_or = num1 > num2 or num3 < num4 # T or T -> T
print(result_or)

result_or = num1 < num2 or num3 < num4 # F or T -> T
print(result_or)

result_or = num1 < num2 or num3 > num4 # F or F -> F
print(result_or)

print("==============")

result_not = num1 < num2 or num3 > num4 # F or F -> F
print(result_not)
print(not result_not)

print("==============")

# Membership Operators
data = "python is easy to learn"
find_word = "java"
found = find_word in data
print(found)

data = "python is easy to learn"
find_word = "python"
found = find_word in data
print(found)


# Employees -> 10
employee_ids = [101,102,103,104,105,106,107,108,109,110]
find_emp = 125
found = find_emp in employee_ids
print(found)

# Employees -> 10
employee_ids = [101,102,103,104,105,106,107,108,109,110]
find_emp = 125
found = find_emp not in employee_ids
print(found)

# data = 1001
# find_word = 0
# found = find_word in data # TypeError: argument of type 'int' is not iterable
# print(found)

