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


# Without Return 
def add(a,b):
    a + b

add(10,20)
print(add(10,20))

# With Return 
def add(a,b):
    return a + b

add(10,20)
print(add(10,20))

def add(a,b):
    return a + b
    print("See if this code executes") # Code is structurally unreachable
print(add(100,200))

def math_ops(a,b):
    return a + b
    return a - b
    return a * b

print(math_ops(30,20))

def math_ops(a,b,opr):
    if opr == "+":
        return a + b
    elif opr == "-":
        return a - b
    elif opr == "*":
        return a * b
    else:
        return "Invalid Operator Selected"
    
print(math_ops(20,10,"+"))
print(math_ops(20,10,"-"))
print(math_ops(20,10,"*"))
print(math_ops(20,10,"/"))

# Function Composition 
def add(a,b):
    return a+b

def sub(c,d,e): # add c+d then minus e
    return add(c,d) - e 

print(sub(3,4,5)) 

def greet():
    return "Hello"

def morning():
    print(greet())
    return "Good Morning"

print(morning())

# Local Scope
def add():
    la = 10 # local variables
    lb = 5
    print(la) # accessed within function 
    print(lb)
    
add()

# print(la)  # accessed outside function # NameError: name 'la' is not defined. Did you mean: 'a'?

# Local Scope
def add(la,lb):
    print(la) # accessed within function 
    print(lb)
    
add(3000,2000)

# print(la) NameError: name 'la' is not defined. Did you mean: 'a'?

# global variable 
ga = 30 

def add(la,lb):
    print(la)
    print(lb)
    print(ga) # global accessed within function 
    
add(10,20)
print(ga) # global accessed outside the function 

# global variable 
ga = 30 

# name conflict 
def add(la,lb,ga): # here ga is local 
    print(la)
    print(lb)
    print(ga)
    print(globals()['ga'])
    
add(1,2,3)

# global keyword scenario 
count = 0
count += 1
print(count)

count = 0
def increment():
    global count
    count += 1
increment()
print(count)

# Built In Functions 
# type, len, max, min, dir, id, input
print(type(count))
print(id(count))

# Built In Functions via modules
import random
random_value = random.randint(1000,9999)
print(random_value)

# External Functions via modules
import requests
response = requests.get('https://www.python.org/')
print(response.status_code)

response = requests.get('https://www.python.org/ravi')
print(response.status_code)

if response.status_code != 200 :
    print("Resource Not Found")
else:
    print("Resource Found")
    
# User Defined Function i.e Without Lambda 
def add(a,b):
    return a+b 
print(add(10,20))

# With Lambda Function
# lambda arguments : expression
sum = lambda a,b : a+b
print(sum(20,30))

# With Lambda Function IILE 
print((lambda a,b : a+b)(200,300))

# without lambda 
def is_even_num(num):
    if num % 2 == 0:
        return True 
    else:
        return False 

print(is_even_num(5))
print(is_even_num(10))

# with lambda
# print((lambda a,b : a+b)(200,300))
print((lambda num : num % 2 == 0)(11))
print((lambda num : num % 2 == 0)(13))
print((lambda num : num % 2 == 0)(12))


# without lambda 
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(0))

# This will cause a syntax error:    
# (lambda num: 
#     if num > 0:
#         "Positive"
#     elif num < 0:
#         "Negative"
#     else:
#         "Zero"
# )(0)

# print((lambda num : "Positive" if num > 0 elif num < 0 "Negative" else "Zero")(0))

# ✔ You can use nested conditional expressions (a if cond1 else b if cond2 else c)

# ❌ You cannot use elif directly inside a lambda

# with lambda using conditions checks 
# check for num is positive, negative and zero
print((lambda num : "Positive" if num > 0 else "Negative" if num < 0 else "Zero")(0))


employee_info = lambda emp_name,emp_email,emp_location: print(f"Hi {emp_name}, your email is {emp_email} and work location is {emp_location}")
employee_info(emp_name="ravi",emp_location="hyderabad",emp_email="ravi@gmail.com")