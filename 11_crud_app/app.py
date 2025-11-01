# Student Management System

# menu based system ==> in future replace with UI elements like buttons 

# System Setup Info On Start up
SYSTEM_INFO = ("Edify Technologies","Student Management System","v1")

# Admin Info at end
ADMIN_INFO = ("9090880","admin@edify.com")

# set student details in dictionary 
students = {}

# Start Up Info
print("="*50)
print(f"Welcome To {SYSTEM_INFO[0]}")
print(f"Software Name {SYSTEM_INFO[1]} {SYSTEM_INFO[2]}")
print("="*50)

# menu based system
while True:
    print("Choose An Option: ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List Student")
    print("5 - Exit Application")
    
    choice = input("Enter Choice (1-5): ")
    
    if choice == "1":
        print("Adding Student")
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("Student already exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("Score should be (0-100)")
                else:
                    print("Invalid Score, only digits allowed")
                    
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input)
            
            # save student details to dictionary
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print("Student Added")
            print(students) # for confirmation i.e test
                   
            
        
    elif choice == "2":
        print("Updating Student")
    elif choice == "3":
        print("Deleting Student")
    elif choice == "4":
        print("Listing Student")
    elif choice == "5":
        print("Exiting Application")
        print("="*50)
        print(f"Contact Admin : {ADMIN_INFO[0]}")
        print(f"Email Admin: {ADMIN_INFO[1]}")
        print("="*50)
        break
    else:
        print("Invalid Choice, Please select (1-5)")
        

