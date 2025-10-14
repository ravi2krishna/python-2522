# Loops - Repetition 

# while loop 
    # You can use while loop, when you don't know 
    # number of iterations in advance 

# Password Auth 
password = "login@123"
user_given_password = ""

while user_given_password != password:
    user_given_password = input("Enter Password: ")
    
print("Password Matched, Login Success")