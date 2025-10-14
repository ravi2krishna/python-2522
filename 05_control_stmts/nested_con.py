# Vote App
age = int(input("Enter Your Age: ")) # type casting
if age >= 18: 
    has_id = input("Do You Have id (yes/no): ")
    if has_id == "yes":
        print("You Can Vote")
    else:
        print("You Need an id to vote") 
else:
    print("You Cannot Vote")