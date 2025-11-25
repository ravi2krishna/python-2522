# Student Blueprint
class Student:
    
    # class variables shared across all instances/objects of this class
    institute_name = "Edify"
    
    # constructor with instance data 
    def __init__(self, student_id, student_name, student_age, student_email, student_mobile_number):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_email = student_email
        self.student_mobile_number = student_mobile_number
    
    # class method -> display institute info 
    @classmethod
    def institute_info(cls):
        print("=" * 50)
        print("             Welcome To: "+Student.institute_name)
        print("=" * 50)
    
    # instance method -> display basic student info -> hover functionality 
    def student_basic_info(self):
        print("=" * 50)
        print("             Basic Student Information")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print("=" * 50)
    
    # instance method -> display complete student info -> click functionality 
    def student_basic_info(self):
        print("=" * 50)
        print("             Complete Student Information")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")
        print(f"Student Age: {self.student_age}")
        print(f"Student Email: {self.student_email}")
        print(f"Student Mobile: {self.student_mobile_number}")
        print("=" * 50)
        
    # calculate sessions credits 
    def sessions_credits_cal(self):
        # local variables
        sessions_credits = 0
        total_sessions_attended = int(input("Enter Total Sessions Attended: "))
        if total_sessions_attended >= 30:
            sessions_credits = 5
        elif total_sessions_attended >= 20:
            sessions_credits = 3
        else:
            sessions_credits = 0
        return sessions_credits
    
    # calculate score credits 
    def score_credits_cal(self,score):
        # local variables
        score_credits = 0
        if score >= 85:
            score_credits = 5
        elif score >= 60:
            score_credits = 3
        else:
            score_credits = 0
        return score_credits
    
    # calculate achievement status (combining sessions credits & score credits)
    
    
        