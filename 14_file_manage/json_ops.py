# Working With JSON Data / Files 

student = {
    "id": 101,
    "name": "Ravi",
    "email": "ravi2krishna@gmail.com",
    "courses": ["python","django","ai"],
    "gpa": 8.5
}

print(type(student))
print(student)

# Writing Dictionary Data As JSON File 
import json
with open("14_file_manage/student.json","w") as file_data:
    json.dump(student,file_data)

# Writing Dictionary Data As JSON File 
import json
with open("14_file_manage/stu.json","w") as file_data:
    json.dump(student,file_data,indent=4)

    