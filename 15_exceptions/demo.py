# Exception Handling 

# when there is no error -> Nothing To Handle 
print("Program Execution Started")
num1 = 10
num2 = 5

print(num1/num2)

print("Program Execution Completed")

print("=" * 50)

# when there is error -> python handles by stopping the program
print("Program Execution Started")
num1 = 10
num2 = 0

# print(num1/num2) # ZeroDivisionError: division by zero

print("Program Execution Completed")

print("=" * 50)

# try : used to keep the code, that will cause error 
# except : used to keep the code that should run, when error occurs 

# when there is error -> user handles the errors using try & except 

print("Program Execution Started")
num1 = 10
num2 = 0

# when there is error -> user handles errors by try & catch with meaningful info
try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide a number by zero - It's a Math Rule")
    print("Check Out More Info On - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

print("Program Execution Started")
num1 = 10
num2 = 5

# when there is error -> user handles errors by try & catch with meaningful info
try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide a number by zero - It's a Math Rule")
    print("Check Out More Info On - https://en.wikipedia.org/wiki/Division_by_zero")

print("Program Execution Completed")

print("=" * 50)

# When we have multiple errors 
print("Program Execution Started")
# data = [1,2,'python',0,5]
# data = [1,2,0,5]
data = [1,2,5]
for num in data:
    print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    # in future i might get more errors 
    
print("Program Execution Completed")

print("=" * 50)


# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    # in future i might get more errors 
    except:
        print("OOPS! Something Went Wrong")
    
print("Program Execution Completed")

print("=" * 50)


# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    # in future i might get more errors 
    except:
        print("OOPS! Dividing String With Number Is Not Supported")
    # except:
    #     print("OOPS! You cannot divide a number by zero - It's a Math Rule")
    
print("Program Execution Completed")

print("=" * 50)

# When we have multiple errors 
print("Program Execution Started")
data = [1,2,'python',0,5]
for num in data:
    try:
        print(1/num) 
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    # ZeroDivisionError: division by zero
    # in future i might get more errors 
    except TypeError:
        print("OOPS! Dividing String With Number Is Not Supported")
    except ZeroDivisionError:
        print("OOPS! You cannot divide a number by zero - It's a Math Rule")
    
print("Program Execution Completed")

print("=" * 50)


print("Program Execution Started")
num1 = 10
num2 = 0

# when there is error -> user handles errors by try & catch with meaningful info
try:
    print(num1/num2) # ZeroDivisionError: division by zero
except:
    print("OOPS! You cannot divide a number by zero - It's a Math Rule")
    print("Check Out More Info On - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("calculation success")
finally:
    print("Program Execution Completed")
print("=" * 50)
    

