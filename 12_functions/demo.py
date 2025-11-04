# Without Functions

a = 10
b = 5

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)


a = 20
b = 10

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 200
b = 100

# math operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("="*50)

# with functions 
def math_ops():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

a = 20
b = 10
math_ops()
a = 200
b = 100
math_ops()
a = 2000
b = 1000
math_ops()

print("=" * 50)

# with functions using parameters 
def math_ops(a,b): # a & b are parameters 
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# math_ops() # TypeError: math_ops() missing 2 required positional arguments: 'a' and 'b'
math_ops(20,10) # 20,10 are arguments   
math_ops(200,100) 
math_ops(2000,1000) 



# Positional Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

# employee_info() # TypeError: employee_info() missing 3 required positional arguments: 'emp_name', 'emp_email', and 'emp_location'
# employee_info("ravi")  # TypeError: employee_info() missing 2 required positional arguments: 'emp_email' and 'emp_location'  
employee_info("ravi","hyderabad","ravi@gmail.com")

def add(a,b,c):
    print(a+b+c)

add(1,2,3)    
add(3,2,1)    # order doesn't matter 


# Keyword Arguments
def employee_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")

employee_info(emp_name="ravi",emp_location="hyderabad",emp_email="ravi@gmail.com")


# No Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")

employee_info(emp_name="ravi",emp_location="hyderabad",emp_email="ravi@gmail.com",org_name="Google")
employee_info(emp_name="john",emp_location="new york",emp_email="john@gmail.com",org_name="Google")

# Default Arguments
def employee_info(emp_name,emp_email,emp_location,org_name="Google"):
    print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")

employee_info(emp_name="ravi",emp_location="hyderabad",emp_email="ravi@gmail.com")
employee_info(emp_name="john",emp_location="new york",emp_email="john@gmail.com")

employee_info(emp_name="mike",emp_location="new york",emp_email="mike@gmail.com",org_name="META")

# Attempting to place a non-default argument after a default argument will result in a SyntaxError.
# def employee_info(emp_name,emp_email,emp_location,org_name="Google",emp_mobile):
#     print(f"Hi {emp_name}, your email is {emp_email} and working for {org_name} at location {emp_location}")


# Arbitrary Positional Arguments
def add_numbers(*nums): # def add_numbers(10,20,30)
    total_sum = 0
    for num in nums:
        total_sum = total_sum + num
    print(f"The Total Sum: {total_sum}")
     
add_numbers(10)
add_numbers(10,20)
add_numbers(10,20,30)
add_numbers(10,20,30,40,50,60)
    
# Arbitrary Keywords Arguments
def profile(**info):
    print(info)
    
profile(fname="Ravi")
profile(fname="Ravi",lname="Krishna",age=20)

def bank_transactions(**trans):
    print(trans)
    total = 0
    for tran in trans:
        # print(trans[tran])
        total = total + trans[tran]
    print(f"You have done total {len(trans)} transactions for a total of {total}")

bank_transactions(jan=1000,feb=2000,mar=5000)    
bank_transactions(apr=6000,may=7000)    

    