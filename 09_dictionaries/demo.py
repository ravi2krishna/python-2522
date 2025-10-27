# Dictionaries

# Empty Dictionary  
empty_dict = {}
print(empty_dict)
print(type(empty_dict))

# Empty Dictionary  
empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# dictionary with numeric data 
# num_dict = {10,20,30,40,50} 
num_dict = {1:10,2:20,3:30} 
print(type(num_dict))
print(num_dict)

# dictionary with text data 
text_dict = {"course1":"python","course2":"django","course3":"ai"}
print(text_dict)

# dictionary with mixed data 
mixed_dict = {10:20,30:"thirty","student_pass":True}
print(mixed_dict)

# Duplicates - values
num_dict = {1:10,2:20,3:30,4:30,5:30} 
print(type(num_dict))
print(num_dict)

# Duplicates - keys
num_dict = {1:10,2:20,2:20.0,1:0,3:30,1:5} 
print(type(num_dict))
print(num_dict)

# Keys should be immutable objects
# num_dict = {[10]:10,2:20,3:30,4:30,5:30} 
num_dict = {(10):10,2:20,3:30,4:30,5:30} 
print(type(num_dict))
print(num_dict)